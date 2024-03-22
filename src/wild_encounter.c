#include "../include/global.h"
#include "../include/random.h"
#include "../include/wild_encounter.h"
#include "../include/event_data.h"
#include "../include/fieldmap.h"
#include "../include/random.h"
#include "../include/roamer.h"
#include "../include/field_player_avatar.h"
#include "../include/battle_setup.h"
#include "../include/overworld.h"
#include "../include/metatile_behavior.h"
#include "../include/event_scripts.h"
#include "../include/script.h"
#include "../include/link.h"
#include "../include/quest_log.h"
#include "../include/constants/maps.h"
#include "../include/constants/abilities.h"
#include "../include/constants/items.h"

enum
{
    WILD_AREA_LAND,
    WILD_AREA_WATER,
    WILD_AREA_ROCKS,
    WILD_AREA_FISHING,
};

#define WILD_CHECK_REPEL    0x1
#define WILD_CHECK_KEEN_EYE 0x2

bool8 TryGenerateWildMonLevelScaling(const struct WildPokemonInfo * info, u8 area, u8 flags)
{
    u8 slot = 0;
    u8 level;
    u8 badgeCount = CountBadgesForOverworldWhiteOutLossCalculation();
    switch (area)
    {
    case WILD_AREA_LAND:
        slot = ChooseWildMonIndex_Land();
        break;
    case WILD_AREA_WATER:
        slot = ChooseWildMonIndex_WaterRock();
        break;
    case WILD_AREA_ROCKS:
        slot = ChooseWildMonIndex_WaterRock();
        break;
    }
    level = ChooseWildMonLevel(&info->wildPokemon[slot]);
    if (badgeCount == 0) level = 100;
    if (flags == WILD_CHECK_REPEL && !IsWildLevelAllowedByRepel(level))
    {
        return FALSE;
    }
    GenerateWildMon(info->wildPokemon[slot].species, level, slot);
    return TRUE;
}