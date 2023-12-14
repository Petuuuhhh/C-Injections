#!/usr/bin/env python3
# -*- coding: cp437 -*-

import sys
from insert import TryProcessFileInclusion, TryProcessConditionalCompilation

CharMap = "charmap.tbl"

SpecialBuffers = {
	"SUPER_ER": ["2C"],
	"LV": ["34"],
	"PK": ["53"],
	"PKMN": ["53", "54"],
	"POKEBLOCK": ["55", "56", "57", "58", "59"],
	"UP_ARROW": ["79"],
	"DOWN_ARROW": ["7A"],
	"LEFT_ARROW": ["7B"],
	"RIGHT_ARROW": ["7C"],
	"SUPER_E": ["84"],
	"SUPER_RE": ["A0"],
	"TALL_PLUS": ["FC", "0C", "FB"],
	"STRING": ["FD"],
	"PLAYER": ["FD", "01"],
	"STR_VAR_1": ["FD", "02"],
	"STR_VAR_2": ["FD", "03"],
	"STR_VAR_3": ["FD", "04"],
	"KUN": ["FD", "05"],
	"RIVAL": ["FD", "06"],
	"VERSION": ["FD", "07"],
	"EVIL_TEAM": ["FD", "08"],
	"GOOD_TEAM": ["FD", "09"],
	"EVIL_LEADER": ["FD", "0A"],
	"GOOD_LEADER": ["FD", "0B"],
	"EVIL_LEGENDARY": ["FD", "0C"],
	"GOOD_LEGENDARY": ["FD", "0D"],
	"UNKNOWN_STR": ["FD", "00"],
	"ATTACKING_TRAINER": ["FD", "08"],
	"DEFENDING_TRAINER": ["FD", "09"],
	"ATTACKING_MON": ["FD", "0C"],
	"DEFENDING_MON": ["FD", "0D"],
	"B_BUFF1": ["FD", "00"],
	"B_BUFF2": ["FD", "01"],
	"B_COPY_VAR_1": ["FD", "02"],
	"B_COPY_VAR_2": ["FD", "03"],
	"B_COPY_VAR_3": ["FD", "04"],
	"B_PLAYER_MON1_NAME": ["FD", "05"],
	"B_OPPONENT_MON1_NAME": ["FD", "06"],
	"B_PLAYER_MON2_NAME": ["FD", "07"],
	"B_OPPONENT_MON2_NAME": ["FD", "08"],
	"B_LINK_PLAYER_MON1_NAME": ["FD", "09"],
	"B_LINK_OPPONENT_MON1_NAME": ["FD", "0A"],
	"B_LINK_PLAYER_MON2_NAME": ["FD", "0B"],
	"B_LINK_OPPONENT_MON2_NAME": ["FD", "0C"],
	"B_ATK_NAME_WITH_PREFIX_MON1": ["FD", "0D"],
	"B_ATK_PARTNER_NAME": ["FD", "0E"],
	"B_ATK_NAME_WITH_PREFIX": ["FD", "0F"],
	"B_DEF_NAME_WITH_PREFIX": ["FD", "10"],
	"B_EFF_NAME_WITH_PREFIX": ["FD", "11"],
	"B_ACTIVE_NAME_WITH_PREFIX": ["FD", "12"],
	"B_SCR_ACTIVE_NAME_WITH_PREFIX": ["FD", "13"],
	"B_CURRENT_MOVE": ["FD", "14"],
	"B_LAST_MOVE": ["FD", "15"],
	"B_LAST_ITEM": ["FD", "16"],
	"B_LAST_ABILITY": ["FD", "17"],
	"B_ATK_ABILITY": ["FD", "18"],
	"B_DEF_ABILITY": ["FD", "19"],
	"B_SCR_ACTIVE_ABILITY": ["FD", "1A"],
	"B_EFF_ABILITY": ["FD", "1B"],
	"B_TRAINER1_CLASS": ["FD", "1C"],
	"B_TRAINER1_NAME": ["FD", "1D"],
	"B_LINK_PLAYER_NAME": ["FD", "1E"],
	"B_LINK_PARTNER_NAME": ["FD", "1F"],
	"B_LINK_OPPONENT1_NAME": ["FD", "20"],
	"B_LINK_OPPONENT2_NAME": ["FD", "21"],
	"B_LINK_SCR_TRAINER_NAME": ["FD", "22"],
	"B_PLAYER_NAME": ["FD", "23"],
	"B_TRAINER1_LOSE_TEXT": ["FD", "24"],
	"B_TRAINER1_WIN_TEXT": ["FD", "25"],
	"B_26": ["FD", "26"],
	"B_PC_CREATOR_NAME": ["FD", "27"],
	"B_ATK_PREFIX1": ["FD", "28"],
	"B_DEF_PREFIX1": ["FD", "29"],
	"B_ATK_PREFIX2": ["FD", "2A"],
	"B_DEF_PREFIX2": ["FD", "2B"],
	"B_ATK_PREFIX3": ["FD", "2C"],
	"B_DEF_PREFIX3": ["FD", "2D"],
	"B_TRAINER2_LOSE_TEXT": ["FD", "2E"],
	"B_TRAINER2_WIN_TEXT": ["FD", "2F"],
	"B_BUFF3": ["FD", "30"],
	"NAME_END": ["FC", "00"],
	"DYNAMIC": ["", "", "F7"],
	"COLOR": ["FC", "01"],
	"HIGHLIGHT": ["FC", "02"],
	"SHADOW": ["FC", "03"],
	"COLOR_HIGHLIGHT_SHADOW": ["FC", "04"],
	"PALETTE": ["FC", "05"],
	"FONT": ["FC", "06"],
	"RESET_FONT": ["FC", "07"],
	"PAUSE": ["FC", "08"],
	"PAUSE_UNTIL_PRESS": ["FC", "09"],
	"WAIT_SE": ["FC", "0A"],
	"PLAY_BGM": ["FC", "0B"],
	"ESCAPE": ["FC", "0C"],
	"SHIFT_RIGHT": ["FC", "0D"],
	"SHIFT_DOWN": ["FC", "0E"],
	"FILL_WINDOW": ["FC", "0F"],
	"PLAY_SE": ["FC", "10"],
	"CLEAR": ["FC", "11"],
	"SKIP": ["FC", "12"],
	"CLEAR_TO": ["FC", "13"],
	"MIN_LETTER_SPACING": ["FC", "14"],
	"JPN": ["FC", "15"],
	"ENG": ["FC", "16"],
	"PAUSE_MUSIC": ["FC", "17"],
	"RESUME_MUSIC": ["FC", "18"],
	"FONT_SMALL": ["FC", "06", "00"],
	"FONT_NORMAL_COPY_1": ["FC", "06", "01"],
	"FONT_NORMAL": ["FC", "06", "02"],
	"FONT_NORMAL_COPY_2": ["FC", "06", "03"],
	"FONT_MALE": ["FC", "06", "04"],
	"FONT_FEMALE": ["FC", "06", "05"],
	"TRANSPARENT": ["00"],
	"WHITE": ["01"],
	"DARK_GRAY": ["02"],
	"LIGHT_GRAY": ["03"],
	"RED": ["04"],
	"LIGHT_RED": ["05"],
	"GREEN": ["06"],
	"LIGHT_GREEN": ["07"],
	"BLUE": ["08"],
	"LIGHT_BLUE": ["09"],
	"DYNAMIC_COLOR1": ["0A"],
	"DYNAMIC_COLOR2": ["0B"],
	"DYNAMIC_COLOR3": ["0C"],
	"DYNAMIC_COLOR4": ["0D"],
	"DYNAMIC_COLOR5": ["0E"],
	"DYNAMIC_COLOR6": ["0F"],
	"MUS_DUMMY": ["00", "00"],
	"SE_USE_ITEM": ["01", "00"],
	"SE_PC_LOGIN": ["02", "00"],
	"SE_PC_OFF": ["03", "00"],
	"SE_PC_ON": ["04", "00"],
	"SE_SELECT": ["05", "00"],
	"SE_WIN_OPEN": ["06", "00"],
	"SE_WALL_HIT": ["07", "00"],
	"SE_RS_DOOR": ["08", "00"],
	"SE_EXIT": ["09", "00"],
	"SE_LEDGE": ["0A", "00"],
	"SE_BIKE_BELL": ["0B", "00"],
	"SE_NOT_EFFECTIVE": ["0C", "00"],
	"SE_EFFECTIVE": ["0D", "00"],
	"SE_SUPER_EFFECTIVE": ["0E", "00"],
	"SE_BALL_OPEN": ["0F", "00"],
	"SE_FAINT": ["10", "00"],
	"SE_FLEE": ["11", "00"],
	"SE_SLIDING_DOOR": ["12", "00"],
	"SE_SHIP": ["13", "00"],
	"SE_BANG": ["14", "00"],
	"SE_PIN": ["15", "00"],
	"SE_BOO": ["16", "00"],
	"SE_BALL": ["17", "00"],
	"SE_CONTEST_PLACE": ["18", "00"],
	"SE_SUCCESS": ["19", "00"],
	"SE_FAILURE": ["1A", "00"],
	"SE_EXP": ["1B", "00"],
	"SE_BIKE_HOP": ["1C", "00"],
	"SE_SWITCH": ["1D", "00"],
	"SE_CLICK": ["1E", "00"],
	"SE_FU_ZAKU": ["1F", "00"],
	"SE_CONTEST_CONDITION_LOSE": ["20", "00"],
	"SE_LAVARIDGE_FALL_WARP": ["21", "00"],
	"SE_ICE_STAIRS": ["22", "00"],
	"SE_ICE_BREAK": ["23", "00"],
	"SE_ICE_CRACK": ["24", "00"],
	"SE_FALL": ["25", "00"],
	"SE_UNLOCK": ["26", "00"],
	"SE_WARP_IN": ["27", "00"],
	"SE_WARP_OUT": ["28", "00"],
	"SE_REPEL": ["29", "00"],
	"SE_ROTATING_GATE": ["2A", "00"],
	"SE_TRUCK_MOVE": ["2B", "00"],
	"SE_TRUCK_STOP": ["2C", "00"],
	"SE_TRUCK_UNLOAD": ["2D", "00"],
	"SE_TRUCK_DOOR": ["2E", "00"],
	"SE_BERRY_BLENDER": ["2F", "00"],
	"SE_SAVE": ["30", "00"],
	"SE_BALL_BOUNCE_1": ["31", "00"],
	"SE_BALL_BOUNCE_2": ["32", "00"],
	"SE_BALL_BOUNCE_3": ["33", "00"],
	"SE_BALL_BOUNCE_4": ["34", "00"],
	"SE_BALL_TRADE": ["35", "00"],
	"SE_BALL_THROW": ["36", "00"],
	"SE_NOTE_C": ["37", "00"],
	"SE_NOTE_D": ["38", "00"],
	"SE_NOTE_E": ["39", "00"],
	"SE_NOTE_F": ["3A", "00"],
	"SE_NOTE_G": ["3B", "00"],
	"SE_NOTE_A": ["3C", "00"],
	"SE_NOTE_B": ["3D", "00"],
	"SE_NOTE_C_HIGH": ["3E", "00"],
	"SE_PUDDLE": ["3F", "00"],
	"SE_BRIDGE_WALK": ["40", "00"],
	"SE_ITEMFINDER": ["41", "00"],
	"SE_DING_DONG": ["42", "00"],
	"SE_BALLOON_RED": ["43", "00"],
	"SE_BALLOON_BLUE": ["44", "00"],
	"SE_BALLOON_YELLOW": ["45", "00"],
	"SE_BREAKABLE_DOOR": ["46", "00"],
	"SE_MUD_BALL": ["47", "00"],
	"SE_FIELD_POISON": ["48", "00"],
	"SE_ESCALATOR": ["49", "00"],
	"SE_THUNDERSTORM": ["4A", "00"],
	"SE_THUNDERSTORM_STOP": ["4B", "00"],
	"SE_DOWNPOUR": ["4C", "00"],
	"SE_DOWNPOUR_STOP": ["4D", "00"],
	"SE_RAIN": ["4E", "00"],
	"SE_RAIN_STOP": ["4F", "00"],
	"SE_THUNDER": ["50", "00"],
	"SE_THUNDER2": ["51", "00"],
	"SE_ELEVATOR": ["52", "00"],
	"SE_LOW_HEALTH": ["53", "00"],
	"SE_EXP_MAX": ["54", "00"],
	"SE_ROULETTE_BALL": ["55", "00"],
	"SE_ROULETTE_BALL2": ["56", "00"],
	"SE_TAILLOW_WING_FLAP": ["57", "00"],
	"SE_RS_SHOP": ["58", "00"],
	"SE_CONTEST_HEART": ["59", "00"],
	"SE_CONTEST_CURTAIN_RISE": ["5A", "00"],
	"SE_CONTEST_CURTAIN_FALL": ["5B", "00"],
	"SE_CONTEST_ICON_CHANGE": ["5C", "00"],
	"SE_CONTEST_ICON_CLEAR": ["5D", "00"],
	"SE_CONTEST_MONS_TURN": ["5E", "00"],
	"SE_SHINY": ["5F", "00"],
	"SE_INTRO_BLAST": ["60", "00"],
	"SE_MUGSHOT": ["61", "00"],
	"SE_APPLAUSE": ["62", "00"],
	"SE_VEND": ["63", "00"],
	"SE_ORB": ["64", "00"],
	"SE_DEX_SCROLL": ["65", "00"],
	"SE_DEX_PAGE": ["66", "00"],
	"SE_POKENAV_ON": ["67", "00"],
	"SE_POKENAV_OFF": ["68", "00"],
	"SE_DEX_SEARCH": ["69", "00"],
	"SE_EGG_HATCH": ["6A", "00"],
	"SE_BALL_TRAY_ENTER": ["6B", "00"],
	"SE_BALL_TRAY_BALL": ["6C", "00"],
	"SE_BALL_TRAY_EXIT": ["6D", "00"],
	"SE_GLASS_FLUTE": ["6E", "00"],
	"SE_M_THUNDERBOLT": ["6F", "00"],
	"SE_M_THUNDERBOLT2": ["70", "00"],
	"SE_M_HARDEN": ["71", "00"],
	"SE_M_NIGHTMARE": ["72", "00"],
	"SE_M_VITAL_THROW": ["73", "00"],
	"SE_M_VITAL_THROW2": ["74", "00"],
	"SE_M_BUBBLE": ["75", "00"],
	"SE_M_BUBBLE2": ["76", "00"],
	"SE_M_BUBBLE3": ["77", "00"],
	"SE_M_RAIN_DANCE": ["78", "00"],
	"SE_M_CUT": ["79", "00"],
	"SE_M_STRING_SHOT": ["7A", "00"],
	"SE_M_STRING_SHOT2": ["7B", "00"],
	"SE_M_ROCK_THROW": ["7C", "00"],
	"SE_M_GUST": ["7D", "00"],
	"SE_M_GUST2": ["7E", "00"],
	"SE_M_DOUBLE_SLAP": ["7F", "00"],
	"SE_M_DOUBLE_TEAM": ["80", "00"],
	"SE_M_RAZOR_WIND": ["81", "00"],
	"SE_M_ICY_WIND": ["82", "00"],
	"SE_M_THUNDER_WAVE": ["83", "00"],
	"SE_M_COMET_PUNCH": ["84", "00"],
	"SE_M_MEGA_KICK": ["85", "00"],
	"SE_M_MEGA_KICK2": ["86", "00"],
	"SE_M_CRABHAMMER": ["87", "00"],
	"SE_M_JUMP_KICK": ["88", "00"],
	"SE_M_FLAME_WHEEL": ["89", "00"],
	"SE_M_FLAME_WHEEL2": ["8A", "00"],
	"SE_M_FLAMETHROWER": ["8B", "00"],
	"SE_M_FIRE_PUNCH": ["8C", "00"],
	"SE_M_TOXIC": ["8D", "00"],
	"SE_M_SACRED_FIRE": ["8E", "00"],
	"SE_M_SACRED_FIRE2": ["8F", "00"],
	"SE_M_EMBER": ["90", "00"],
	"SE_M_TAKE_DOWN": ["91", "00"],
	"SE_M_BLIZZARD": ["92", "00"],
	"SE_M_BLIZZARD2": ["93", "00"],
	"SE_M_SCRATCH": ["94", "00"],
	"SE_M_VICEGRIP": ["95", "00"],
	"SE_M_WING_ATTACK": ["96", "00"],
	"SE_M_FLY": ["97", "00"],
	"SE_M_SAND_ATTACK": ["98", "00"],
	"SE_M_RAZOR_WIND2": ["99", "00"],
	"SE_M_BITE": ["9A", "00"],
	"SE_M_HEADBUTT": ["9B", "00"],
	"SE_M_SURF": ["9C", "00"],
	"SE_M_HYDRO_PUMP": ["9D", "00"],
	"SE_M_WHIRLPOOL": ["9E", "00"],
	"SE_M_HORN_ATTACK": ["9F", "00"],
	"SE_M_TAIL_WHIP": ["A0", "00"],
	"SE_M_MIST": ["A1", "00"],
	"SE_M_POISON_POWDER": ["A2", "00"],
	"SE_M_BIND": ["A3", "00"],
	"SE_M_DRAGON_RAGE": ["A4", "00"],
	"SE_M_SING": ["A5", "00"],
	"SE_M_PERISH_SONG": ["A6", "00"],
	"SE_M_PAY_DAY": ["A7", "00"],
	"SE_M_DIG": ["A8", "00"],
	"SE_M_DIZZY_PUNCH": ["A9", "00"],
	"SE_M_SELF_DESTRUCT": ["AA", "00"],
	"SE_M_EXPLOSION": ["AB", "00"],
	"SE_M_ABSORB_2": ["AC", "00"],
	"SE_M_ABSORB": ["AD", "00"],
	"SE_M_SCREECH": ["AE", "00"],
	"SE_M_BUBBLE_BEAM": ["AF", "00"],
	"SE_M_BUBBLE_BEAM2": ["B0", "00"],
	"SE_M_SUPERSONIC": ["B1", "00"],
	"SE_M_BELLY_DRUM": ["B2", "00"],
	"SE_M_METRONOME": ["B3", "00"],
	"SE_M_BONEMERANG": ["B4", "00"],
	"SE_M_LICK": ["B5", "00"],
	"SE_M_PSYBEAM": ["B6", "00"],
	"SE_M_FAINT_ATTACK": ["B7", "00"],
	"SE_M_SWORDS_DANCE": ["B8", "00"],
	"SE_M_LEER": ["B9", "00"],
	"SE_M_SWAGGER": ["BA", "00"],
	"SE_M_SWAGGER2": ["BB", "00"],
	"SE_M_HEAL_BELL": ["BC", "00"],
	"SE_M_CONFUSE_RAY": ["BD", "00"],
	"SE_M_SNORE": ["BE", "00"],
	"SE_M_BRICK_BREAK": ["BF", "00"],
	"SE_M_GIGA_DRAIN": ["C0", "00"],
	"SE_M_PSYBEAM2": ["C1", "00"],
	"SE_M_SOLAR_BEAM": ["C2", "00"],
	"SE_M_PETAL_DANCE": ["C3", "00"],
	"SE_M_TELEPORT": ["C4", "00"],
	"SE_M_MINIMIZE": ["C5", "00"],
	"SE_M_SKETCH": ["C6", "00"],
	"SE_M_SWIFT": ["C7", "00"],
	"SE_M_REFLECT": ["C8", "00"],
	"SE_M_BARRIER": ["C9", "00"],
	"SE_M_DETECT": ["CA", "00"],
	"SE_M_LOCK_ON": ["CB", "00"],
	"SE_M_MOONLIGHT": ["CC", "00"],
	"SE_M_CHARM": ["CD", "00"],
	"SE_M_CHARGE": ["CE", "00"],
	"SE_M_STRENGTH": ["CF", "00"],
	"SE_M_HYPER_BEAM": ["D0", "00"],
	"SE_M_WATERFALL": ["D1", "00"],
	"SE_M_REVERSAL": ["D2", "00"],
	"SE_M_ACID_ARMOR": ["D3", "00"],
	"SE_M_SANDSTORM": ["D4", "00"],
	"SE_M_TRI_ATTACK": ["D5", "00"],
	"SE_M_TRI_ATTACK2": ["D6", "00"],
	"SE_M_ENCORE": ["D7", "00"],
	"SE_M_ENCORE2": ["D8", "00"],
	"SE_M_BATON_PASS": ["D9", "00"],
	"SE_M_MILK_DRINK": ["DA", "00"],
	"SE_M_ATTRACT": ["DB", "00"],
	"SE_M_ATTRACT2": ["DC", "00"],
	"SE_M_MORNING_SUN": ["DD", "00"],
	"SE_M_FLATTER": ["DE", "00"],
	"SE_M_SAND_TOMB": ["DF", "00"],
	"SE_M_GRASSWHISTLE": ["E0", "00"],
	"SE_M_SPIT_UP": ["E1", "00"],
	"SE_M_DIVE": ["E2", "00"],
	"SE_M_EARTHQUAKE": ["E3", "00"],
	"SE_M_TWISTER": ["E4", "00"],
	"SE_M_SWEET_SCENT": ["E5", "00"],
	"SE_M_YAWN": ["E6", "00"],
	"SE_M_SKY_UPPERCUT": ["E7", "00"],
	"SE_M_STAT_INCREASE": ["E8", "00"],
	"SE_M_HEAT_WAVE": ["E9", "00"],
	"SE_M_UPROAR": ["EA", "00"],
	"SE_M_HAIL": ["EB", "00"],
	"SE_M_COSMIC_POWER": ["EC", "00"],
	"SE_M_TEETER_DANCE": ["ED", "00"],
	"SE_M_STAT_DECREASE": ["EE", "00"],
	"SE_M_HAZE": ["EF", "00"],
	"SE_M_HYPER_BEAM2": ["F0", "00"],
	"SE_DOOR": ["F1", "00"],
	"SE_CARD_FLIP": ["F2", "00"],
	"SE_CARD_FLIPPING": ["F3", "00"],
	"SE_CARD_OPEN": ["F4", "00"],
	"SE_BAG_CURSOR": ["F5", "00"],
	"SE_BAG_POCKET": ["F6", "00"],
	"SE_BALL_CLICK": ["F7", "00"],
	"SE_SHOP": ["F8", "00"],
	"SE_SS_ANNE_HORN": ["F9", "00"],
	"SE_HELP_OPEN": ["FA", "00"],
	"SE_HELP_CLOSE": ["FB", "00"],
	"SE_HELP_ERROR": ["FC", "00"],
	"SE_DEOXYS_MOVE": ["FD", "00"],
	"SE_POKE_JUMP_SUCCESS": ["FE", "00"],
	"SE_POKE_JUMP_FAILURE": ["FF", "00"],
	"MUS_HEAL": ["00", "01"],
	"MUS_LEVEL_UP": ["01", "01"],
	"MUS_OBTAIN_ITEM": ["02", "01"],
	"MUS_EVOLVED": ["03", "01"],
	"MUS_OBTAIN_BADGE": ["04", "01"],
	"MUS_OBTAIN_TMHM": ["05", "01"],
	"MUS_OBTAIN_BERRY": ["06", "01"],
	"MUS_EVOLUTION_INTRO": ["07", "01"],
	"MUS_EVOLUTION": ["08", "01"],
	"MUS_RS_VS_GYM_LEADER": ["09", "01"],
	"MUS_RS_VS_TRAINER": ["0A", "01"],
	"MUS_SCHOOL": ["0B", "01"],
	"MUS_SLOTS_JACKPOT": ["0C", "01"],
	"MUS_SLOTS_WIN": ["0D", "01"],
	"MUS_MOVE_DELETED": ["0E", "01"],
	"MUS_TOO_BAD": ["0F", "01"],
	"MUS_FOLLOW_ME": ["10", "01"],
	"MUS_GAME_CORNER": ["11", "01"],
	"MUS_ROCKET_HIDEOUT": ["12", "01"],
	"MUS_GYM": ["13", "01"],
	"MUS_JIGGLYPUFF": ["14", "01"],
	"MUS_INTRO_FIGHT": ["15", "01"],
	"MUS_TITLE": ["16", "01"],
	"MUS_CINNABAR": ["17", "01"],
	"MUS_LAVENDER": ["18", "01"],
	"MUS_HEAL_UNUSED": ["19", "01"],
	"MUS_CYCLING": ["1A", "01"],
	"MUS_ENCOUNTER_ROCKET": ["1B", "01"],
	"MUS_ENCOUNTER_GIRL": ["1C", "01"],
	"MUS_ENCOUNTER_BOY": ["1D", "01"],
	"MUS_HALL_OF_FAME": ["1E", "01"],
	"MUS_VIRIDIAN_FOREST": ["1F", "01"],
	"MUS_MT_MOON": ["20", "01"],
	"MUS_POKE_MANSION": ["21", "01"],
	"MUS_CREDITS": ["22", "01"],
	"MUS_ROUTE1": ["23", "01"],
	"MUS_ROUTE24": ["24", "01"],
	"MUS_ROUTE3": ["25", "01"],
	"MUS_ROUTE11": ["26", "01"],
	"MUS_VICTORY_ROAD": ["27", "01"],
	"MUS_VS_GYM_LEADER": ["28", "01"],
	"MUS_VS_TRAINER": ["29", "01"],
	"MUS_VS_WILD": ["2A", "01"],
	"MUS_VS_CHAMPION": ["2B", "01"],
	"MUS_PALLET": ["2C", "01"],
	"MUS_OAK_LAB": ["2D", "01"],
	"MUS_OAK": ["2E", "01"],
	"MUS_POKE_CENTER": ["2F", "01"],
	"MUS_SS_ANNE": ["30", "01"],
	"MUS_SURF": ["31", "01"],
	"MUS_POKE_TOWER": ["32", "01"],
	"MUS_SILPH": ["33", "01"],
	"MUS_FUCHSIA": ["34", "01"],
	"MUS_CELADON": ["35", "01"],
	"MUS_VICTORY_TRAINER": ["36", "01"],
	"MUS_VICTORY_WILD": ["37", "01"],
	"MUS_VICTORY_GYM_LEADER": ["38", "01"],
	"MUS_VERMILLION": ["39", "01"],
	"MUS_PEWTER": ["3A", "01"],
	"MUS_ENCOUNTER_RIVAL": ["3B", "01"],
	"MUS_RIVAL_EXIT": ["3C", "01"],
	"MUS_DEX_RATING": ["3D", "01"],
	"MUS_OBTAIN_KEY_ITEM": ["3E", "01"],
	"MUS_CAUGHT_INTRO": ["3F", "01"],
	"MUS_PHOTO": ["40", "01"],
	"MUS_GAME_FREAK": ["41", "01"],
	"MUS_CAUGHT": ["42", "01"],
	"MUS_NEW_GAME_INSTRUCT": ["43", "01"],
	"MUS_NEW_GAME_INTRO": ["44", "01"],
	"MUS_NEW_GAME_EXIT": ["45", "01"],
	"MUS_POKE_JUMP": ["46", "01"],
	"MUS_UNION_ROOM": ["47", "01"],
	"MUS_NET_CENTER": ["48", "01"],
	"MUS_MYSTERY_GIFT": ["49", "01"],
	"MUS_BERRY_PICK": ["4A", "01"],
	"MUS_SEVII_CAVE": ["4B", "01"],
	"MUS_TEACHY_TV_SHOW": ["4C", "01"],
	"MUS_SEVII_ROUTE": ["4D", "01"],
	"MUS_SEVII_DUNGEON": ["4E", "01"],
	"MUS_SEVII_123": ["4F", "01"],
	"MUS_SEVII_45": ["50", "01"],
	"MUS_SEVII_67": ["51", "01"],
	"MUS_POKE_FLUTE": ["52", "01"],
	"MUS_VS_DEOXYS": ["53", "01"],
	"MUS_VS_MEWTWO": ["54", "01"],
	"MUS_VS_LEGEND": ["55", "01"],
	"MUS_ENCOUNTER_GYM_LEADER": ["56", "01"],
	"MUS_ENCOUNTER_DEOXYS": ["57", "01"],
	"MUS_TRAINER_TOWER": ["58", "01"],
	"MUS_SLOW_PALLET": ["59", "01"],
	"MUS_TEACHY_TV_MENU": ["5A", "01"],
	"A_BUTTON": ["F8", "00"],
	"B_BUTTON": ["F8", "01"],
	"L_BUTTON": ["F8", "02"],
	"R_BUTTON": ["F8", "03"],
	"START_BUTTON": ["F8", "04"],
	"SELECT_BUTTON": ["F8", "05"],
	"DPAD_UP": ["F8", "06"],
	"DPAD_DOWN": ["F8", "07"],
	"DPAD_LEFT": ["F8", "08"],
	"DPAD_RIGHT": ["F8", "09"],
	"DPAD_UPDOWN": ["F8", "0A"],
	"DPAD_LEFTRIGHT": ["F8", "0B"],
	"DPAD_ANY": ["F8", "0C"],
	"UP_ARROW_2": ["F9", "00"],
	"DOWN_ARROW_2": ["F9", "01"],
	"LEFT_ARROW_2": ["F9", "02"],
	"RIGHT_ARROW_2": ["F9", "03"],
	"PLUS": ["F9", "04"],
	"LV_2": ["F9", "05"],
	"PP": ["F9", "06"],
	"ID": ["F9", "07"],
	"NO": ["F9", "08"],
	"UNDERSCORE": ["F9", "09"],
	"CIRCLE_1": ["F9", "0A"],
	"CIRCLE_2": ["F9", "0B"],
	"CIRCLE_3": ["F9", "0C"],
	"CIRCLE_4": ["F9", "0D"],
	"CIRCLE_5": ["F9", "0E"],
	"CIRCLE_6": ["F9", "0F"],
	"CIRCLE_7": ["F9", "10"],
	"CIRCLE_8": ["F9", "11"],
	"CIRCLE_9": ["F9", "12"],
	"LEFT_PAREN": ["F9", "13"],
	"RIGHT_PAREN": ["F9", "14"],
	"CIRCLE_DOT": ["F9", "15"],
	"TRIANGLE": ["F9", "16"],
	"BIG_MULT_X": ["F9", "17"],
	"EMOJI_UNDERSCORE": ["F9", "D0"],
	"EMOJI_PIPE": ["F9", "D1"],
	"EMOJI_HIGHBAR": ["F9", "D2"],
	"EMOJI_TILDE": ["F9", "D3"],
	"EMOJI_LEFT_PAREN": ["F9", "D4"],
	"EMOJI_RIGHT_PAREN": ["F9", "D5"],
	"EMOJI_UNION": ["F9", "D6"],
	"EMOJI_GREATER_THAN": ["F9", "D7"],
	"EMOJI_LEFT_EYE": ["F9", "D8"],
	"EMOJI_RIGHT_EYE": ["F9", "D9"],
	"EMOJI_AT": ["F9", "DA"],
	"EMOJI_SEMICOLON": ["F9", "DB"],
	"EMOJI_PLUS": ["F9", "DC"],
	"EMOJI_MINUS": ["F9", "DD"],
	"EMOJI_EQUALS": ["F9", "DE"],
	"EMOJI_SPIRAL": ["F9", "DF"],
	"EMOJI_TONGUE": ["F9", "E0"],
	"EMOJI_TRIANGLE_OUTLINE": ["F9", "E1"],
	"EMOJI_ACUTE": ["F9", "E2"],
	"EMOJI_GRAVE": ["F9", "E3"],
	"EMOJI_CIRCLE": ["F9", "E4"],
	"EMOJI_TRIANGLE": ["F9", "E5"],
	"EMOJI_SQUARE": ["F9", "E6"],
	"EMOJI_HEART": ["F9", "E7"],
	"EMOJI_MOON": ["F9", "E8"],
	"EMOJI_NOTE": ["F9", "E9"],
	"EMOJI_BALL": ["F9", "EA"],
	"EMOJI_BOLT": ["F9", "EB"],
	"EMOJI_LEAF": ["F9", "EC"],
	"EMOJI_FIRE": ["F9", "ED"],
	"EMOJI_WATER": ["F9", "EE"],
	"EMOJI_LEFT_FIST": ["F9", "EF"],
	"EMOJI_RIGHT_FIST": ["F9", "F0"],
	"EMOJI_BIGWHEEL": ["F9", "F1"],
	"EMOJI_SMALLWHEEL": ["F9", "F2"],
	"EMOJI_SPHERE": ["F9", "F3"],
	"EMOJI_IRRITATED": ["F9", "F4"],
	"EMOJI_MISCHIEVOUS": ["F9", "F5"],
	"EMOJI_HAPPY": ["F9", "F6"],
	"EMOJI_ANGRY": ["F9", "F7"],
	"EMOJI_SURPRISED": ["F9", "F8"],
	"EMOJI_BIGSMILE": ["F9", "F9"],
	"EMOJI_EVIL": ["F9", "FA"],
	"EMOJI_TIRED": ["F9", "FB"],
	"EMOJI_NEUTRAL": ["F9", "FC"],
	"EMOJI_SHOCKED": ["F9", "FD"],
	"EMOJI_BIGANGER": ["F9", "FE"],
}


def StringFileConverter(fileName: str):
    stringToWrite = ".thumb\n.text\n.align 2\n\n"
    with open(fileName, 'r', encoding="ISO-8859-1") as file:
        maxLength = 0
        fillFF = False
        readingState = 0
        lineNum = 0
        definesDict = {}
        conditionals = []

        for line in file:
            lineNum += 1
            line = line.rstrip("\n\r")  # Remove only newline characters
            if TryProcessFileInclusion(line, definesDict):
                continue
            if TryProcessConditionalCompilation(line, definesDict, conditionals):
                continue
            if line.strip() == "" or line[:2] == "//":  # Ignore blank lines and comment lines
                continue
            
            if readingState == 0:  # Only when the file starts
                line = line.strip()
                if line[:6].upper() == "#ORG @" and line[6:] != "":
                    title = line[6:]
                    stringToWrite += ".global " + title + "\n" + title + ":\n"
                    readingState = 1
                elif "MAX_LENGTH" in line and "=" in line:
                    try:
                        maxLength = int(line.split("=")[1])
                    except:
                        print('Error reading max length on line ' + str(lineNum) + ' in file: "' + fileName + '"')
                        sys.exit(0)
                elif "FILL_FF" in line and "=" in line:
                    try:
                        fillFF = bool(line.split("=")[1])
                    except:
                        print('Error reading FF fill on line ' + str(lineNum) + ' in file: "' + fileName + '"')
                        sys.exit(0)
                else:
                    print('Warning! Error on line ' + str(lineNum) + ' in file: "' + fileName + '"')
                    
            elif readingState == 1:
                if line[:6].upper() == "#ORG @" and line[6:] != "":
                    line = line.strip()
                    title = line[6:]
                    stringToWrite += ".global " + title + "\n" + title + ":\n"
                else:
                    stringToWrite += ProcessString(line, lineNum, maxLength, fillFF)
                    stringToWrite += "0xFF\n\n"  # Only print line in everything went alright

    output = open(fileName.split(".string")[0] + '.s', 'w')  # Only open file once we know everything went okay.
    output.write(stringToWrite)
    output.close()


def ProcessString(string: str, lineNum: int, maxLength=0, fillWithFF=False) -> str:
    charMap = PokeByteTableMaker()
    stringToWrite = ".byte "
    buffer = False
    escapeChar = False
    bufferChars = ""
    strLen = 0

    for char in string.encode('iso-8859-1').decode('utf-8'):
        if 0 < maxLength <= strLen:
            print('Warning: The string "' + string + '" has exceeded the maximum length of '
                  + str(maxLength) + ' and has been truncated!')
            break

        if buffer is True:
            if char == ']':
                buffer = False

                if bufferChars in SpecialBuffers:
                    for bufferChar in SpecialBuffers[bufferChars]:
                        if 0 < maxLength <= strLen:  # End buffer in middle
                            print('Warning: The string buffer "' + bufferChars + '" has exceeded the maximum length of '
                                  + str(maxLength) + ' and has been truncated!')
                            break

                        stringToWrite += ("0x" + bufferChar + ", ")
                        strLen += 1

                elif len(bufferChars.split(' ')) > 1:  # Unrecognized buffer
                    for bufferChar in bufferChars.split(' '):
                        if bufferChar in SpecialBuffers:
                            for buffChar in SpecialBuffers[bufferChar]:
                                stringToWrite += ("0x" + buffChar + ", ")
                                strLen += 1
                        else:
                            # if int(bufferChar, 16) > 255:
                                # pass # do something
                            stringToWrite += ("0x" + bufferChar.replace('0x', '') + ", ")
                            strLen += 1

                bufferChars = ""
            else:
                bufferChars += char

        elif escapeChar is True:
            escapeChar = False
            try:
                stringToWrite += hex(charMap["\\" + char]) + ", "
                strLen += 1

            except KeyError:
                print(char, string.index(char))
                print('Error parsing string: "' + string + '" (Line ' + str(lineNum) + ')')
                sys.exit(0)

        else:
            try:
                stringToWrite += hex(charMap[char]) + ", "
                strLen += 1

            except KeyError:
                if char == '[':
                    buffer = True
                elif char == '\\':
                    escapeChar = True
                elif char == '"':
                    stringToWrite += hex(charMap["\\" + char])
                    strLen += 1
                else:
                    print(char)
                    print('Error parsing string on line ' + str(lineNum) + ' at character "' + char + '".')
                    sys.exit(1)
    
    if strLen < maxLength and fillWithFF:
        while strLen < maxLength:
            stringToWrite += "0xFF, "
            strLen += 1

    return stringToWrite


def PokeByteTableMaker():
    dictionary = {}
    with open(CharMap, 'r', encoding='iso-8859-1') as file:
        for line in file:
            if line.strip() != "/FF" and line.strip() != "":
                if line[2] == '=' and line[3] != "":
                    try:
                        dictionary[line[3:].encode('iso-8859-1').decode('utf-8')[:-1]] = int(line.split('=')[0], 16)
                    except:
                        pass
        dictionary[' '] = 0
    return dictionary
