#include "../include/global.h"
#include "../include/malloc.h"
#include "../include/bg.h"
#include "../include/decompress.h"
#include "../include/gpu_regs.h"
#include "../include/palette.h"
#include "../include/graphics.h"
#include "../include/task.h"
#include "../include/text.h"
#include "../include/text_window.h"
#include "../include/menu.h"
#include "../include/menu_helpers.h"
#include "../include/new_menu_helpers.h"
#include "../include/list_menu.h"
#include "../include/item.h"
#include "../include/item_menu.h"
#include "../include/link.h"
#include "../include/money.h"
#include "../include/shop.h"
#include "../include/teachy_tv.h"
#include "../include/pokemon_storage_system.h"
#include "../include/string_util.h"
#include "../include/party_menu.h"
#include "../include/data.h"
#include "../include/scanline_effect.h"
#include "../include/sound.h"
#include "../include/strings.h"
#include "../include/menu_indicators.h"
#include "../include/constants/items.h"
#include "../include/constants/songs.h"

#define TAG_DISC 400

u8 *gText_FontSize0 = (u8 *)0x084166ff; // ?
u8 *sText_ClearTo18 = (u8 *)0x08463178;
u8 *gOtherText_UnkF9_08_Clear_01 = (u8 *)0x08416226;
u8 *sText_SingleSpace = (u8 *)0x0846317c;
u8 *gText_FontSize2 = (u8 *)0x08416703; // ?
// IDs for the actions in the context menu
enum {
    ACTION_USE,
    ACTION_GIVE,
    ACTION_EXIT
};
// sTMCaseDynamicResources 0203b118
// The "dynamic" resources will be reset any time the TM case is exited, even temporarily.
static EWRAM_DATA struct {
    void (* nextScreenCallback)(void);
    u8 discSpriteId;
    u8 maxTMsShown;
    u8 numTMs;
    u8 contextMenuWindowId;
    u8 scrollArrowsTaskId;
    u16 currItem;
    const u8 * menuActionIndices;
    u8 numMenuActions;
    s16 seqId;
    u8 unused[8];
} * sTMCaseDynamicResources = 0x0203B118;
// sMenuActionIndices_Field 08463168
// sMenuActionIndices_UnionRoom 0846316b
static const u8 sMenuActionIndices_Field[] = {ACTION_USE, ACTION_GIVE, ACTION_EXIT};
static const u8 sMenuActionIndices_UnionRoom[] = {ACTION_GIVE, ACTION_EXIT};
enum {
    WIN_LIST,
    WIN_DESCRIPTION,
    WIN_SELECTED_MSG,
    WIN_TITLE,
    WIN_MOVE_INFO_LABELS,
    WIN_MOVE_INFO,
    WIN_MESSAGE,
    WIN_SELL_QUANTITY,
    WIN_MONEY,
};
enum {
    COLOR_LIGHT,
    COLOR_DARK,
    COLOR_CURSOR_SELECTED,
    COLOR_MOVE_INFO,
    COLOR_CURSOR_ERASE = 0xFF
};
#define tListTaskId       data[0]
#define tSelection        data[1]
static void Action_Use(u8 taskId)
{
    RemoveContextMenu(&sTMCaseDynamicResources->contextMenuWindowId);
    ClearStdWindowAndFrameToTransparent(WIN_SELECTED_MSG, FALSE);
    ClearWindowTilemap(WIN_SELECTED_MSG);
    PutWindowTilemap(WIN_LIST);
    ScheduleBgCopyTilemapToVram(0);
    ScheduleBgCopyTilemapToVram(1);
    if (CalculatePlayerPartyCount() == 0)
    {
        PrintError_ThereIsNoPokemon(taskId);
    }
    else
    {
        // Chose a TM/HM to use, exit TM case for party menu
        gItemUseCB = ItemUseCB_TMHM;
        sTMCaseDynamicResources->nextScreenCallback = CB2_ShowPartyMenuForItemUse;
        Task_BeginFadeOutFromTMCase(taskId);
    }
}

#define IS_HM(itemId) (ItemId_GetImportance(itemId) != 0)

static void Action_Give(u8 taskId)
{
    s16 * data = gTasks[taskId].data;
    u16 itemId = BagGetItemIdByPocketPosition(POCKET_TM_CASE, tSelection);
    RemoveContextMenu(&sTMCaseDynamicResources->contextMenuWindowId);
    ClearStdWindowAndFrameToTransparent(WIN_SELECTED_MSG, FALSE);
    ClearWindowTilemap(WIN_SELECTED_MSG);
    PutWindowTilemap(WIN_DESCRIPTION);
    PutWindowTilemap(WIN_MOVE_INFO_LABELS);
    PutWindowTilemap(WIN_MOVE_INFO);
    ScheduleBgCopyTilemapToVram(0);
    ScheduleBgCopyTilemapToVram(1);
    if (!IS_HM(itemId))
    {
        if (CalculatePlayerPartyCount() == 0)
        {
            PrintError_ThereIsNoPokemon(taskId);
        }
        else
        {
            sTMCaseDynamicResources->nextScreenCallback = CB2_ChooseMonToGiveItem;
            Task_BeginFadeOutFromTMCase(taskId);
        }
    }
    else
    {
        PrintError_ItemCantBeHeld(taskId);
    }
}

static void Action_Exit(u8 taskId)
{
    s16 * data = gTasks[taskId].data;

    RemoveContextMenu(&sTMCaseDynamicResources->contextMenuWindowId);
    ClearStdWindowAndFrameToTransparent(WIN_SELECTED_MSG, FALSE);
    ClearWindowTilemap(WIN_SELECTED_MSG);
    PutWindowTilemap(WIN_LIST);
    PrintListCursor(tListTaskId, COLOR_DARK);
    PutWindowTilemap(WIN_DESCRIPTION);
    PutWindowTilemap(WIN_MOVE_INFO_LABELS);
    PutWindowTilemap(WIN_MOVE_INFO);
    ScheduleBgCopyTilemapToVram(0);
    ScheduleBgCopyTilemapToVram(1);
    ReturnToList(taskId);
}

// 081325f0 l 0000006c Action_Use
// 0813265c l 0000009c Action_Give
// 081327fc l 0000006c Action_Exit
// (*Action_Use)(u8) = (u8 (*)(void))0x081325f1;
static const struct MenuAction sMenuActions_UseGiveExit[] = {
    [ACTION_USE]  = {gOtherText_Use,  Action_Use },
    [ACTION_GIVE] = {gOtherText_Give, Action_Give},
    [ACTION_EXIT] = {gOtherText_Exit, Action_Exit},
};
// sMenuActions_UseGiveExit 084643a8?
// 081325f0 l 0000006c Action_Use
// 0813265c l 0000009c Action_Give
// 081327fc l 0000006c Action_Exit
// 08463150 l 00000018 sMenuActions
// (*sMenuActions_UseGiveExit)(u32) = (u32 (*)(void))0x08463150;
// u8 *sMenuActions_UseGiveExit = (u8 *)0x08463150;
// Task_TMContextMenu_HandleInput 08132568
static void Task_TMContextMenu_HandleInput(u8 taskId)
{
    s8 input;

    if (IsActiveOverworldLinkBusy() != TRUE)
    {
        input = Menu_ProcessInputNoWrapAround();
        switch (input)
        {
        case MENU_B_PRESSED:
            // Run last action in list (Exit)
            PlaySE(SE_SELECT);
            sMenuActions_UseGiveExit[sTMCaseDynamicResources->menuActionIndices[sTMCaseDynamicResources->numMenuActions - 1]].func.void_u8(taskId);
            break;
        case MENU_NOTHING_CHOSEN:
            break;
        default:
            PlaySE(SE_SELECT);
            sMenuActions_UseGiveExit[sTMCaseDynamicResources->menuActionIndices[input]].func.void_u8(taskId);
            break;
        }
    }
}
// sTMSpriteTemplate
// 084631f8 l 00000008 sTMSpriteOamData
u8 *sTMSpriteOamData = (u8 *)0x084631f8;
// 083f1ca8 l 00000003 sTextColors
u8 *sTextColors = (u8 *)0x083f1ca8;
// 08463210 l 00000008 sAnims_Disc
// u8 *sAnims_Disc = (u8 *)0x08463210;
enum {
    ANIM_TM,
    ANIM_HM,
};
static const union AnimCmd sAnim_TM[] = {
    ANIMCMD_FRAME(0, 0),
    ANIMCMD_END
};

static const union AnimCmd sAnim_HM[] = {
    ANIMCMD_FRAME(16, 0),
    ANIMCMD_END
};
static const union AnimCmd *const sAnims_Disc[] = {
    [ANIM_TM] = sAnim_TM,
    [ANIM_HM] = sAnim_HM
};
static const struct SpriteTemplate sTMSpriteTemplate = {
    .tileTag = TAG_DISC,
    .paletteTag = TAG_DISC,
    .oam = &sTMSpriteOamData,
    .anims = sAnims_Disc,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCallbackDummy
};

void GetTMNumberAndMoveString(u8 * dest, u16 itemId)
{
    StringCopy(gStringVar4, gText_FontSize0);
    if (itemId >= ITEM_HM01)
    {
        u8 hmDigits = 1;
        if (NUM_HIDDEN_MACHINES >= 10)
            hmDigits = 2;
        
        StringAppend(gStringVar4, sText_ClearTo18);
        StringAppend(gStringVar4, gOtherText_UnkF9_08_Clear_01);
        ConvertIntToDecimalStringN(gStringVar1, itemId - ITEM_HM01 + 1, STR_CONV_MODE_LEADING_ZEROS, hmDigits);
        StringAppend(gStringVar4, gStringVar1);
    }
    else
    {
        u8 tmDigits = 2;
        if (NUM_TECHNICAL_MACHINES >= 100)
            tmDigits = 3;
        
        StringAppend(gStringVar4, gOtherText_UnkF9_08_Clear_01);
        ConvertIntToDecimalStringN(gStringVar1, itemId - ITEM_TM01 + 1, STR_CONV_MODE_LEADING_ZEROS, tmDigits);
        StringAppend(gStringVar4, gStringVar1);
    }
    
    StringAppend(gStringVar4, sText_SingleSpace);
    StringAppend(gStringVar4, gText_FontSize2);
    StringAppend(gStringVar4, gMoveNames[ItemIdToBattleMoveId(itemId)]);
    StringCopy(dest, gStringVar4);
}

static void AddTextPrinterParameterized_ColorByIndex(u8 windowId, u8 fontId, const u8 * str, u8 x, u8 y, u8 letterSpacing, u8 lineSpacing, u8 speed, u8 colorIdx)
{
    AddTextPrinterParameterized4(windowId, fontId, x, y, letterSpacing, lineSpacing, sTextColors[colorIdx], speed, str);
}

void TMCase_ItemPrintFunc(u8 windowId, s32 itemId, u8 y)
{
    bool8 isHm = FALSE;
    bool8 showQuantity = TRUE;
    
    if (itemId != -2)
    {
        if (BagGetItemIdByPocketPosition(POCKET_TM_CASE, itemId) >= ITEM_HM01)
            isHm = TRUE;
        else
            isHm = FALSE;
        
		#ifdef REUSABLE_TMS
            showQuantity = FALSE;
		#else
            showQuantity = TRUE;
		#endif
        
        if (!isHm)
        {
            if (showQuantity)
            {
                ConvertIntToDecimalStringN(gStringVar1, BagGetQuantityByPocketPosition(POCKET_TM_CASE, itemId), STR_CONV_MODE_RIGHT_ALIGN, 3);
                StringExpandPlaceholders(gStringVar4, gText_TimesStrVar1);
                AddTextPrinterParameterized_ColorByIndex(windowId, 0, gStringVar4, 0x7E, y, 0, 0, 0xFF, 1);
            }
        }
        else
        {
            PlaceHMTileInWindow(windowId, 8, y);
        }
    }
}

static const struct WindowTemplate sTMContextWindowTemplates[] = {
    {0x01, 0x16, 0x0d, 0x07, 0x06, 0x0f, 0x01cf},
    {0x01, 0x16, 0x0f, 0x07, 0x04, 0x0f, 0x01cf}
};

static u8 AddTMContextMenu(u8 * a0, u8 a1)
{
    if (*a0 == 0xFF)
    {
        *a0 = AddWindow(&sTMContextWindowTemplates[a1]);
        TMCase_SetWindowBorder1(*a0);
        ScheduleBgCopyTilemapToVram(0);
    }
    return *a0;
}

#define TM_CASE_TM_TAG 400
static EWRAM_DATA u16 * sTMSpritePaletteBuffer = 0x0203b12c;

static const u16 sTMSpritePaletteOffsetByType[] = {
    [TYPE_NORMAL]   = 0x000,
    [TYPE_FIRE]     = 0x010,
    [TYPE_WATER]    = 0x020,
    [TYPE_GRASS]    = 0x030,
    [TYPE_ELECTRIC] = 0x040,
    [TYPE_ROCK]     = 0x050,
    [TYPE_GROUND]   = 0x060,
    [TYPE_ICE]      = 0x070,
    [TYPE_FLYING]   = 0x080,
    [TYPE_FIGHTING] = 0x090,
    [TYPE_GHOST]    = 0x0a0,
    [TYPE_BUG]      = 0x0b0,
    [TYPE_POISON]   = 0x0c0,
    [TYPE_PSYCHIC]  = 0x0d0,
    [TYPE_STEEL]    = 0x0e0,
    [TYPE_DARK]     = 0x0f0,
    [TYPE_DRAGON]   = 0x100
};

//static const u16 sFairyTmPalette[] = INCBIN_U16("graphics/tm_case/fairy_tm.gbapal");
static EWRAM_DATA struct {
    void (* savedCallback)(void);
    u8 tmCaseMenuType;
    u8 unk_05;
    u8 unk_06;
    u16 selectedRow;
    u16 scrollOffset;
} sTMCaseStaticResources = {};

static void TintTMSpriteByType(u8 type)
{
    u8 palIndex = IndexOfSpritePaletteTag(TM_CASE_TM_TAG) << 4;
    
    /*  if you have fairy-type tm/hms
    if (type == TYPE_FAIRY)
        LoadPalette(sFairyTmPalette, 0x100 | palIndex, 0x20);        
    else
    */

    LoadPalette(sTMSpritePaletteBuffer + sTMSpritePaletteOffsetByType[type], 0x100 | palIndex, 0x20);
    if (sTMCaseStaticResources.tmCaseMenuType == 4)
    {
        BlendPalettes(1 << (0x10 + palIndex), 4, RGB_BLACK);
    }
}

// Window IDs for the context menu that opens when a TM/HM is selected
enum {
    WIN_USE_GIVE_EXIT,
    WIN_GIVE_EXIT,
};

// When a TM/HM in the list is selected in the field, create a context
// menu with a list of actions that can be taken.
void Task_SelectTMAction_FromFieldBag(u8 taskId)
{
    u8 * strbuf;
    TMCase_SetWindowBorder2(2);
    if (!MenuHelpers_LinkSomething() && InUnionRoom() != TRUE)
    {
        AddTMContextMenu(&sTMCaseDynamicResources->contextMenuWindowId, 0);
        sTMCaseDynamicResources->menuActionIndices = sMenuActionIndices_Field;
        sTMCaseDynamicResources->numMenuActions = NELEMS(sMenuActionIndices_Field);
    }
    else
    {
        AddTMContextMenu(&sTMCaseDynamicResources->contextMenuWindowId, 1);
        sTMCaseDynamicResources->menuActionIndices = sMenuActionIndices_UnionRoom;
        sTMCaseDynamicResources->numMenuActions = NELEMS(sMenuActionIndices_UnionRoom);
    }
    AddItemMenuActionTextPrinters(sTMCaseDynamicResources->contextMenuWindowId, 2, GetMenuCursorDimensionByFont(2, 0), 2, 0, GetFontAttribute(2, 1) + 2, sTMCaseDynamicResources->numMenuActions, sMenuActions_UseGiveExit, sTMCaseDynamicResources->menuActionIndices);
    Menu_InitCursor(sTMCaseDynamicResources->contextMenuWindowId, 2, 0, 2, GetFontAttribute(2, 1) + 2, sTMCaseDynamicResources->numMenuActions, 0);
    strbuf = Alloc(256);
    GetTMNumberAndMoveString(strbuf, gSpecialVar_ItemId);
    StringAppend(strbuf, gText_Var1IsSelected + 2); // +2 skips over the stringvar
    AddTextPrinterParameterized_ColorByIndex(2, 2, strbuf, 0, 2, 1, 0, 0, 1);
    Free(strbuf);
    
    if (gSpecialVar_ItemId >= ITEM_HM01)
    {
        PlaceHMTileInWindow(2, 0, 2);
        CopyWindowToVram(2, 2);
    }
    
    ScheduleBgCopyTilemapToVram(0);
    ScheduleBgCopyTilemapToVram(1);
    gTasks[taskId].func = Task_TMContextMenu_HandleInput;
}

void SetTMSpriteAnim(struct Sprite * sprite, u8 idx)
{
    if (idx > NUM_TECHNICAL_MACHINES)
        StartSpriteAnim(sprite, 1);
    else
        StartSpriteAnim(sprite, 0);
}

void UpdateTMSpritePosition(struct Sprite * sprite, u8 tmId)
{
    s32 x, y;
    if (tmId == 0xFF)    //end of tm case
    {
        x = 0x1B;
        y = 0x36;
        sprite->y2 = 0x14;
    }
    else
    {
        if (tmId > NUM_TECHNICAL_MACHINES)
            tmId -= NUM_TECHNICAL_MACHINES;
        else
            tmId += NUM_HIDDEN_MACHINES;
        
        x = 0x29 - (((0xE00 * tmId) / NUM_TMHMS) >> 8);
        y = 0x2E + (((0x800 * tmId) / NUM_TMHMS) >> 8);
    }
    
    sprite->x = x;
    sprite->y = y;
}

u8 CreateTMSprite(u16 itemId)
{
    u8 spriteId = CreateSprite(&sTMSpriteTemplate, 0x29, 0x2E, 0);
    u8 r5;
    if (itemId == ITEM_NONE)
    {
        UpdateTMSpritePosition(&gSprites[spriteId], 0xFF);
        return spriteId;
    }
    else
    {        
        SetTMSpriteAnim(&gSprites[spriteId], itemId - ITEM_TM01);
        TintTMSpriteByType(gBattleMoves[ItemIdToBattleMoveId(itemId)].type);
        UpdateTMSpritePosition(&gSprites[spriteId], itemId - ITEM_TM01);
        return spriteId;
    }
}