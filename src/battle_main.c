#include "../include/global.h"
#include "../include/gflib.h"
#include "../include/battle.h"
#include "../include/battle_anim.h"
#include "../include/battle_ai_script_commands.h"
#include "../include/battle_controllers.h"
#include "../include/battle_interface.h"
#include "../include/battle_main.h"
#include "../include/battle_message.h"
#include "../include/battle_scripts.h"
#include "../include/battle_setup.h"
#include "../include/berry.h"
#include "../include/data.h"
#include "../include/decompress.h"
#include "../include/event_data.h"
#include "../include/evolution_scene.h"
#include "../include/graphics.h"
#include "../include/help_system.h"
#include "../include/item.h"
#include "../include/link.h"
#include "../include/link_rfu.h"
#include "../include/load_save.h"
#include "../include/m4a.h"
#include "../include/party_menu.h"
#include "../include/pokeball.h"
#include "../include/pokedex.h"
#include "../include/quest_log.h"
#include "../include/random.h"
#include "../include/roamer.h"
#include "../include/safari_zone.h"
#include "../include/scanline_effect.h"
#include "../include/task.h"
#include "../include/trig.h"
#include "../include/vs_seeker.h"
#include "../include/util.h"
#include "../include/constants/abilities.h"
#include "../include/constants/battle_move_effects.h"
#include "../include/constants/battle_setup.h"
#include "../include/constants/hold_effects.h"
#include "../include/constants/items.h"
#include "../include/constants/moves.h"
#include "../include/constants/pokemon.h"
#include "../include/constants/songs.h"
#include "../include/constants/trainers.h"
#include "../include/overworld.h"

extern struct Evolution gEvolutionTable[][EVOS_PER_MON];

u8 CreateNPCTrainerPartyBadgeLevelScaling(struct Pokemon *party, u16 trainerNum)
{
    u32 nameHash = 0;
    u32 personalityValue;
    u8 fixedIV;
    s32 i, j;

    if (trainerNum == TRAINER_SECRET_BASE)
        return 0;

    if (gBattleTypeFlags & BATTLE_TYPE_TRAINER
     && !(gBattleTypeFlags & (BATTLE_TYPE_BATTLE_TOWER | BATTLE_TYPE_EREADER_TRAINER | BATTLE_TYPE_TRAINER_TOWER)))
    {
        ZeroEnemyPartyMons();
        for (i = 0; i < gTrainers[trainerNum].partySize; i++)
        {
            u8 badgeCount = CountBadgesForOverworldWhiteOutLossCalculation();

            if (gTrainers[trainerNum].doubleBattle == TRUE)
                personalityValue = 0x80;
            else if (gTrainers[trainerNum].encounterMusic_gender & F_TRAINER_FEMALE)
                personalityValue = 0x78; // Use personality more likely to result in a female Pokémon
            else
                personalityValue = 0x88; // Use personality more likely to result in a male Pokémon

            for (j = 0; gTrainers[trainerNum].trainerName[j] != EOS; j++)
                nameHash += gTrainers[trainerNum].trainerName[j];

            switch (gTrainers[trainerNum].partyFlags)
            {
            case 0:
            {
                const struct TrainerMonNoItemDefaultMoves *partyData = gTrainers[trainerNum].party.NoItemDefaultMoves;
                u8 level = partyData[i].lvl;
                u16 species = partyData[i].species;
                if (gTrainers[gTrainerBattleOpponent_A].trainerClass != TRAINER_CLASS_LEADER) {
                    if (badgeCount == 0) level = (Random() % 4) + 2;
                    else if (badgeCount == 1) level = (Random() % 6) + 8;
                    else if (badgeCount == 2) level = (Random() % 6) + 13;
                    else if (badgeCount == 3) level = (Random() % 6) + 18;
                    else if (badgeCount == 4) level = (Random() % 6) + 23;
                    else if (badgeCount == 5) level = (Random() % 6) + 28;
                    else if (badgeCount == 6) level = (Random() % 6) + 33;
                    else if (badgeCount == 7) level = (Random() % 6) + 38;
                    else if (badgeCount == 8) level = (Random() % 6) + 43;
                }
                else {
                    if (badgeCount == 0) level = (Random() % 6) + 10;
                    if (badgeCount == 1) level = (Random() % 6) + 16;
                    if (badgeCount == 2) level = (Random() % 6) + 21;
                    if (badgeCount == 3) level = (Random() % 6) + 27;
                    if (badgeCount == 4) level = (Random() % 6) + 32;
                    if (badgeCount == 5) level = (Random() % 6) + 38;
                    if (badgeCount == 6) level = (Random() % 6) + 43;
                    if (badgeCount == 7) level = (Random() % 6) + 49;
                }
                if (gEvolutionTable[species][0].method == EVO_LEVEL && gEvolutionTable[species][0].param <= level) species = gEvolutionTable[species][0].targetSpecies;
                if (gEvolutionTable[species][0].method == EVO_LEVEL && gEvolutionTable[species][0].param <= level) species = gEvolutionTable[species][0].targetSpecies;
                for (j = 0; gSpeciesNames[partyData[i].species][j] != EOS; j++)
                    nameHash += gSpeciesNames[partyData[i].species][j];

                personalityValue += nameHash << 8;
                fixedIV = partyData[i].iv * MAX_PER_STAT_IVS / 255;
                CreateMon(&party[i], species, level, fixedIV, TRUE, personalityValue, OT_ID_RANDOM_NO_SHINY, 0);
                break;
            }
            case F_TRAINER_PARTY_CUSTOM_MOVESET:
            {
                const struct TrainerMonNoItemCustomMoves *partyData = gTrainers[trainerNum].party.NoItemCustomMoves;

                for (j = 0; gSpeciesNames[partyData[i].species][j] != EOS; j++)
                    nameHash += gSpeciesNames[partyData[i].species][j];

                personalityValue += nameHash << 8;
                fixedIV = partyData[i].iv * MAX_PER_STAT_IVS / 255;
                CreateMon(&party[i], partyData[i].species, partyData[i].lvl, fixedIV, TRUE, personalityValue, OT_ID_RANDOM_NO_SHINY, 0);

                for (j = 0; j < MAX_MON_MOVES; j++)
                {
                    SetMonData(&party[i], MON_DATA_MOVE1 + j, &partyData[i].moves[j]);
                    SetMonData(&party[i], MON_DATA_PP1 + j, &gBattleMoves[partyData[i].moves[j]].pp);
                }
                break;
            }
            case F_TRAINER_PARTY_HELD_ITEM:
            {
                const struct TrainerMonItemDefaultMoves *partyData = gTrainers[trainerNum].party.ItemDefaultMoves;

                for (j = 0; gSpeciesNames[partyData[i].species][j] != EOS; j++)
                    nameHash += gSpeciesNames[partyData[i].species][j];

                personalityValue += nameHash << 8;
                fixedIV = partyData[i].iv * MAX_PER_STAT_IVS / 255;
                CreateMon(&party[i], partyData[i].species, partyData[i].lvl, fixedIV, TRUE, personalityValue, OT_ID_RANDOM_NO_SHINY, 0);

                SetMonData(&party[i], MON_DATA_HELD_ITEM, &partyData[i].heldItem);
                break;
            }
            case F_TRAINER_PARTY_CUSTOM_MOVESET | F_TRAINER_PARTY_HELD_ITEM:
            {
                const struct TrainerMonItemCustomMoves *partyData = gTrainers[trainerNum].party.ItemCustomMoves;

                for (j = 0; gSpeciesNames[partyData[i].species][j] != EOS; j++)
                    nameHash += gSpeciesNames[partyData[i].species][j];

                personalityValue += nameHash << 8;
                fixedIV = partyData[i].iv * MAX_PER_STAT_IVS / 255;
                CreateMon(&party[i], partyData[i].species, partyData[i].lvl, fixedIV, TRUE, personalityValue, OT_ID_RANDOM_NO_SHINY, 0);
                SetMonData(&party[i], MON_DATA_HELD_ITEM, &partyData[i].heldItem);

                for (j = 0; j < MAX_MON_MOVES; j++)
                {
                    SetMonData(&party[i], MON_DATA_MOVE1 + j, &partyData[i].moves[j]);
                    SetMonData(&party[i], MON_DATA_PP1 + j, &gBattleMoves[partyData[i].moves[j]].pp);
                }
                break;
            }
            }
        }

        gBattleTypeFlags |= gTrainers[trainerNum].doubleBattle;
    }

    return gTrainers[trainerNum].partySize;
}