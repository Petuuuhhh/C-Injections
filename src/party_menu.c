#include "../include/global.h"
#include "../include/gflib.h"
#include "../include/battle.h"
#include "../include/battle_anim.h"
#include "../include/battle_controllers.h"
#include "../include/battle_gfx_sfx_util.h"
#include "../include/battle_interface.h"
#include "../include/battle_tower.h"
#include "../include/berry_pouch.h"
#include "../include/data.h"
#include "../include/decompress.h"
#include "../include/easy_chat.h"
#include "../include/event_data.h"
#include "../include/evolution_scene.h"
#include "../include/field_effect.h"
#include "../include/field_player_avatar.h"
#include "../include/field_fadetransition.h"
#include "../include/field_weather.h"
#include "../include/fieldmap.h"
#include "../include/fldeff.h"
#include "../include/graphics.h"
#include "../include/help_system.h"
#include "../include/item.h"
#include "../include/item_menu.h"
#include "../include/item_use.h"
#include "../include/link.h"
#include "../include/link_rfu.h"
#include "../include/load_save.h"
#include "../include/mail.h"
#include "../include/mail_data.h"
#include "../include/main.h"
#include "../include/menu.h"
#include "../include/menu_helpers.h"
#include "../include/new_menu_helpers.h"
#include "../include/metatile_behavior.h"
#include "../include/overworld.h"
#include "../include/party_menu.h"
#include "../include/player_pc.h"
#include "../include/pokedex.h"
#include "../include/pokemon.h"
#include "../include/pokemon_icon.h"
#include "../include/pokemon_jump.h"
#include "../include/pokemon_special_anim.h"
#include "../include/pokemon_summary_screen.h"
#include "../include/quest_log.h"
#include "../include/region_map.h"
#include "../include/reshow_battle_screen.h"
#include "../include/scanline_effect.h"
#include "../include/script.h"
#include "../include/start_menu.h"
#include "../include/string_util.h"
#include "../include/strings.h"
#include "../include/task.h"
#include "../include/teachy_tv.h"
#include "../include/text_window.h"
#include "../include/tm_case.h"
#include "../include/trade.h"
#include "../include/union_room.h"
#include "../include/constants/battle.h"
#include "../include/constants/easy_chat.h"
#include "../include/constants/field_effects.h"
#include "../include/constants/flags.h"
#include "../include/constants/item_effects.h"
#include "../include/constants/items.h"
#include "../include/constants/maps.h"
#include "../include/constants/moves.h"
#include "../include/constants/pokemon.h"
#include "../include/constants/quest_log.h"
#include "../include/constants/songs.h"
#include "../include/constants/species.h"

#include "tutor_learnsets.h"
#include "party_menu.h"

(*Task_SetSacredAshCB)(u32) = (u32 (*)(void))0x08124fc9;
(*Task_DoLearnedMoveFanfareAfterText)(u32) = (u32 (*)(void))0x08125cf5;

enum
{
    CAN_LEARN_MOVE,
    CANNOT_LEARN_MOVE,
    ALREADY_KNOWS_MOVE,
    CANNOT_LEARN_MOVE_IS_EGG
};

u16 GetTutorMove(u8 tutor)
{
    switch (tutor)
    {
    case TUTOR_MOVE_FRENZY_PLANT:
        return MOVE_FRENZY_PLANT;
    case TUTOR_MOVE_BLAST_BURN:
        return MOVE_BLAST_BURN;
    case TUTOR_MOVE_HYDRO_CANNON:
        return MOVE_HYDRO_CANNON;
    default:
        return sTutorMoves[tutor];
    }
}

static bool8 CanLearnTutorMove(u16 species, u8 tutor)
{
    switch (tutor)
    {
    case TUTOR_MOVE_FRENZY_PLANT:
        if (species == SPECIES_VENUSAUR)
            return TRUE;
        else
            return FALSE;
    case TUTOR_MOVE_BLAST_BURN:
        if (species == SPECIES_CHARIZARD)
            return TRUE;
        else
            return FALSE;
    case TUTOR_MOVE_HYDRO_CANNON:
        if (species == SPECIES_BLASTOISE)
            return TRUE;
        else
            return FALSE;
    default:
        if (sTutorLearnsets[species] & (1 << tutor))
            return TRUE;
        else
            return FALSE;
    }
}

u8 CanMonLearnTMTutor(struct Pokemon *mon, u16 item, u8 tutor)
{
    u16 move;

    if (GetMonData(mon, MON_DATA_IS_EGG))
        return CANNOT_LEARN_MOVE_IS_EGG;

    if (item >= ITEM_TM01 && item <= ITEM_HM08)
    {
        if (CanMonLearnTMHM(mon, item - ITEM_TM01))
            move = ItemIdToBattleMoveId(item);
        else
            return CANNOT_LEARN_MOVE;
        do
        {
        } while (0);
    }
    else if (item >= ITEM_TM51)
    {
        if (CanMonLearnTMHM(mon, item - 318))
            move = ItemIdToBattleMoveId(item);
        else
            return CANNOT_LEARN_MOVE;
        do
        {
        } while (0);
    }
    else if (CanLearnTutorMove(GetMonData(mon, MON_DATA_SPECIES), tutor) == FALSE)
    {
        return CANNOT_LEARN_MOVE;
    }
    else
    {
        move = GetTutorMove(tutor);
    }
    if (MonKnowsMove(mon, move) == TRUE)
        return ALREADY_KNOWS_MOVE;
    else
        return CAN_LEARN_MOVE;
}

void CB2_UseItem(void)
{
    if (ItemId_GetPocket(gSpecialVar_ItemId) == POCKET_TM_CASE && PSA_IsCancelDisabled() == TRUE)
    {
        GiveMoveToMon(&gPlayerParty[gPartyMenu.slotId], ItemIdToBattleMoveId(gSpecialVar_ItemId));
        AdjustFriendship(&gPlayerParty[gPartyMenu.slotId], FRIENDSHIP_EVENT_LEARN_TMHM);
        #ifndef REUSABLE_TMS
        if (gSpecialVar_ItemId >= ITEM_FIRST_TM && gSpecialVar_ItemId <= ITEM_LAST_TM)
            RemoveBagItem(gSpecialVar_ItemId, 1);
        #endif
        SetMainCallback2(gPartyMenu.exitCallback);
    }
    else
        InitPartyMenu(gPartyMenu.menuType, KEEP_PARTY_LAYOUT, PARTY_ACTION_CHOOSE_MON, gPartyMenu.slotId, PARTY_MSG_NONE, Task_SetSacredAshCB, gPartyMenu.exitCallback);
}

void CB2_UseTMHMAfterForgettingMove(void)
{
    if (PSA_IsCancelDisabled() == TRUE)
    {
        struct Pokemon *mon = &gPlayerParty[gPartyMenu.slotId];
        u8 moveIdx = GetMoveSlotToReplace();
        u16 move = GetMonData(mon, moveIdx + MON_DATA_MOVE1);
        
        RemoveMonPPBonus(mon, moveIdx);
        SetMonMoveSlot(mon, ItemIdToBattleMoveId(gSpecialVar_ItemId), moveIdx);
        AdjustFriendship(mon, FRIENDSHIP_EVENT_LEARN_TMHM);
        ItemUse_SetQuestLogEvent(QL_EVENT_USED_ITEM, mon, gSpecialVar_ItemId, move);
        #ifndef REUSABLE_TMS
        if (gSpecialVar_ItemId >= ITEM_FIRST_TM && gSpecialVar_ItemId <= ITEM_LAST_TM)
            RemoveBagItem(gSpecialVar_ItemId, 1);
        #endif
        SetMainCallback2(gPartyMenu.exitCallback);
    }
    else
        InitPartyMenu(gPartyMenu.menuType, KEEP_PARTY_LAYOUT, gPartyMenu.action, gPartyMenu.slotId, PARTY_MSG_NONE, Task_SetSacredAshCB, gPartyMenu.exitCallback);
}

u16 ItemIdToBattleMoveId(u16 item)
{
    u16 tmNumber;
    if (item >= ITEM_TM01 && item <= ITEM_HM08) tmNumber = item - ITEM_TM01;
    else if (item >= ITEM_TM51) tmNumber = item - 318;

    return sTMHMMoves[tmNumber];
}

void Task_LearnedMove(u8 taskId)
{
    struct Pokemon *mon = &gPlayerParty[gPartyMenu.slotId];
    s16 *move = &gPartyMenu.data1;
    u16 item = gSpecialVar_ItemId;

    if (move[1] == 0)
    {
        AdjustFriendship(mon, 4);
        #ifndef REUSABLE_TMS
        if (gSpecialVar_ItemId >= ITEM_FIRST_TM && gSpecialVar_ItemId <= ITEM_LAST_TM)
            RemoveBagItem(item, 1);
        #endif
    }
    GetMonNickname(mon, gStringVar1);
    StringCopy(gStringVar2, gMoveNames[move[0]]);
    StringExpandPlaceholders(gStringVar4, gText_PkmnLearnedMove3);
    DisplayPartyMenuMessage(gStringVar4, TRUE);
    ScheduleBgCopyTilemapToVram(2);
    gTasks[taskId].func = Task_DoLearnedMoveFanfareAfterText;
}