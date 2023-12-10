#include "../include/global.h"
#include "../include/gflib.h"
#include "../include/script.h"
#include "../include/task.h"
#include "../include/data.h"
#include "../include/trig.h"
#include "../include/field_fadetransition.h"
#include "../include/overworld.h"
#include "../include/new_menu_helpers.h"
#include "../include/menu.h"
#include "../include/list_menu.h"
#include "../include/event_data.h"
#include "../include/text_window.h"
#include "../include/pokemon_summary_screen.h"
#include "../include/graphics.h"
#include "../include/strings.h"
#include "../include/constants/songs.h"
#include "../include/constants/moves.h"

struct LearnMoveGfxResources
{
    u8 state;
    u8 unk_01;
    u8 unk_02;
    u8 spriteIds[2];
    u8 filler_05[0x13];
    u8 unk_18;
    u8 scrollPositionMaybe;
    u8 numLearnableMoves;
    u8 unk_1B;
    u8 unk_1C;
    u8 unk_1D;
    u8 unk_1E;
    struct ListMenuItem listMenuItems[255];
    u16 learnableMoves[255];
    u8 listMenuStrbufs[255][13];
    bool8 scheduleMoveInfoUpdate;
    u8 selectedPartyMember;
    u8 selectedMoveSlot;
    u8 unk_262;
    u8 listMenuTaskId;
    u8 bg1TilemapBuffer[BG_SCREEN_SIZE]; // 264
    u8 textColor[3]; // A64
    u8 selectedIndex;
    u16 listMenuScrollPos;
    u16 listMenuScrollRow;
};

static EWRAM_DATA struct LearnMoveGfxResources * sMoveRelearner = 0x0203aab4;

static void MoveRelearnerMenu_MoveCursorFunc(s32 itemIndex, bool8 onInit, struct ListMenu *list)
{
    if (!onInit)
    {
        PlaySE(SE_SELECT);
        sMoveRelearner->scheduleMoveInfoUpdate = TRUE;
        sMoveRelearner->selectedIndex = itemIndex;
    }
}

static const struct ListMenuTemplate sMoveRelearnerListMenuTemplate = {
    .items = NULL,
    .moveCursorFunc = MoveRelearnerMenu_MoveCursorFunc,
    .itemPrintFunc = NULL,
    .totalItems = 0,
    .maxShowed = 7,
    .windowId = 6,
    .header_X = 0,
    .item_X = 8,
    .cursor_X = 0,
    .upText_Y = 0,
    .cursorPal = 2,
    .fillValue = 1,
    .cursorShadowPal = 3,
    .lettersSpacing = 1,
    .itemVerticalPadding = 0,
    .scrollMultiple = 0,
    .fontId = FONT_NORMAL,
    .cursorKind = 0,
};

#include "move_learner_moves.h"
#define MOVE_LEARNER_MOVES_ARRAY_COUNT           255

u8 GetMoveLearnerMoves(struct Pokemon *pokemon, u16 *moveLearnerMoves)
{
    u16 moveLearnerMoveIdx;
    u16 numMoveLearnerMoves;
    u16 species;
    u16 i;

    numMoveLearnerMoves = 0;
    moveLearnerMoveIdx = 0;
    species = GetMonData(pokemon, MON_DATA_SPECIES);
    for (i = 0; i < NELEMS(gMoveLearnerMoves) - 1; i++)
    {
        if (gMoveLearnerMoves[i] == species + MOVE_LEARNER_MOVES_SPECIES_OFFSET)
        {
            moveLearnerMoveIdx = i + 1;
            break;
        }
    }

    for (i = 0; i < MOVE_LEARNER_MOVES_ARRAY_COUNT; i++)
    {
        if (gMoveLearnerMoves[moveLearnerMoveIdx + i] > MOVE_LEARNER_MOVES_SPECIES_OFFSET)
        {
            // TODO: the curly braces around this if statement are required for a matching build.
            break;
        }

        moveLearnerMoves[i] = gMoveLearnerMoves[moveLearnerMoveIdx + i];
        numMoveLearnerMoves++;
    }

    return numMoveLearnerMoves;
}

void MoveLearnerInitListMenuBuffersEtc(void)
{
    int i;
    s32 count;
    u8 nickname[11];

    if (!FlagGet(FLAG_MOVE_LEARNER)) {
        sMoveRelearner->numLearnableMoves = GetMoveRelearnerMoves(&gPlayerParty[sMoveRelearner->selectedPartyMember], sMoveRelearner->learnableMoves);
        count = GetMoveRelearnerMoves(&gPlayerParty[sMoveRelearner->selectedPartyMember], sMoveRelearner->learnableMoves);
    }
    else {
        sMoveRelearner->numLearnableMoves = GetMoveLearnerMoves(&gPlayerParty[sMoveRelearner->selectedPartyMember], sMoveRelearner->learnableMoves);
        count = GetMoveLearnerMoves(&gPlayerParty[sMoveRelearner->selectedPartyMember], sMoveRelearner->learnableMoves);
    }
    for (i = 0; i < sMoveRelearner->numLearnableMoves; i++)
        StringCopy(sMoveRelearner->listMenuStrbufs[i], gMoveNames[sMoveRelearner->learnableMoves[i]]);
    GetMonData(&gPlayerParty[sMoveRelearner->selectedPartyMember], MON_DATA_NICKNAME, nickname);
    StringCopy_Nickname(gStringVar1, nickname);
    StringCopy(sMoveRelearner->listMenuStrbufs[sMoveRelearner->numLearnableMoves], gFameCheckerText_Cancel);
    sMoveRelearner->numLearnableMoves++;
    for (i = 0; i < count; i++)
    {
        sMoveRelearner->listMenuItems[i].label = sMoveRelearner->listMenuStrbufs[i];
        sMoveRelearner->listMenuItems[i].index = i;
    }
    sMoveRelearner->listMenuItems[i].label = gFameCheckerText_Cancel;
    sMoveRelearner->listMenuItems[i].index = 0xFE;
    gMultiuseListMenuTemplate = sMoveRelearnerListMenuTemplate;
    gMultiuseListMenuTemplate.items = sMoveRelearner->listMenuItems;
    gMultiuseListMenuTemplate.totalItems = count + 1;
}