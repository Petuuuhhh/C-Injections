#define IS_POKEMON_C

#include "../include/global.h"
#include "../include/pokemon.h"
#include "../include/random.h"
#include "../include/main.h"
#include "../include/text.h"
#include "../include/data.h"
#include "../include/string_util.h"
#include "../include/battle.h"
#include "../include/battle_anim.h"
#include "../include/item.h"
#include "../include/event_data.h"
#include "../include/util.h"
#include "../include/pokemon_storage_system.h"
#include "../include/battle_gfx_sfx_util.h"
#include "../include/battle_controllers.h"
#include "../include/evolution_scene.h"
#include "../include/battle_message.h"
#include "../include/battle_util.h"
#include "../include/link.h"
#include "../include/m4a.h"
#include "../include/sound.h"
#include "../include/pokedex.h"
#include "../include/strings.h"
#include "../include/malloc.h"
#include "../include/overworld.h"
#include "../include/party_menu.h"
#include "../include/field_specials.h"
#include "../include/constants/items.h"
#include "../include/constants/item_effects.h"
#include "../include/constants/species.h"
#include "../include/constants/hoenn_cries.h"
#include "../include/constants/pokemon.h"
#include "../include/constants/abilities.h"
#include "../include/constants/flags.h"
#include "../include/constants/moves.h"
#include "../include/constants/opponents.h"
#include "../include/constants/hold_effects.h"
#include "../include/constants/battle_move_effects.h"

#include "tmhm_learnsets.h"

u32 CanMonLearnTMHM(struct Pokemon *mon, u8 tm)
{
    u16 species = GetMonData(mon, MON_DATA_SPECIES2, 0);
    const u8 *learnableMoves;
    
    if (species == SPECIES_EGG)
        return 0;

    learnableMoves = gTMHMLearnsets[species];
    while(*learnableMoves != 0xFF)
    {
        if(*learnableMoves == tm)
            return TRUE;
        
        learnableMoves++;
    }
    
    return FALSE;
}