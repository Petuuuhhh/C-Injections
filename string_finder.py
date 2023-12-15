import TextScripts
from TextScripts import TextScripts, pokefirered_sym, JapaneseTextScripts
from Japanese import JapaneseChars, Japanese
charMap = {'À': 1, 'Á': 2, 'Â': 3, 'Ç': 4, 'È': 5, 'É': 6, 'Ê': 7, 'Ë': 8, 'Ì': 9, 'Î': 11, 'Ï': 12, 'Ò': 13, 'Ó': 14, 'Ô': 15, 'Œ': 16, 'Ù': 17, 'Ú': 18, 'Û': 19, 'Ñ': 20, 'ß': 21, 'à': 22, 'á': 23, 'ç': 25, 'è': 26, 'é': 27, '\\e': 27, 'ê': 28, 'ë': 29, 'ì': 30, 'î': 32, 'ï': 33, 'ò': 34, 'ó': 35, 'ô': 36, 'œ': 37, 'ù': 38, 'ú': 39, 'û': 40, 'ñ': 41, 'º': 42, 'ª': 43, '&': 45, '+': 46, '=': 53, ';': 54, '¿': 81, '¡': 82, 'Í': 90, '%': 91, '(': 92, ')': 93, 'â': 104, 'í': 111, '<': 133, '>': 134, '0': 161, '1': 162, '2': 163, '3': 164, '4': 165, '5': 166, '6': 167, '7': 168, '8': 169, '9': 170, '!': 171, '?': 172, '.': 173, '-': 174, '·': 175, '…': 176, '"': 177, '“': 177, '\\"': 178, '”': 178, '‘': 179, '’': 180, "'": 180, '♂': 181, '♀': 182, '\\$': 183, ',': 184, '*': 185, '/': 186, 'A': 187, 'B': 188, 'C': 189, 'D': 190, 'E': 191, 'F': 192, 'G': 193, 'H': 194, 'I': 195, 'J': 196, 'K': 197, 'L': 198, 'M': 199, 'N': 200, 'O': 201, 'P': 202, 'Q': 203, 'R': 204, 'S': 205, 'T': 206, 'U': 207, 'V': 208, 'W': 209, 'X': 210, 'Y': 211, 'Z': 212, 'a': 213, 'b': 214, 'c': 215, 'd': 216, 'e': 217, 'f': 218, 'g': 219, 'h': 220, 'i': 221, 'j': 222, 'k': 223, 'l': 224, 'm': 225, 'n': 226, 'o': 227, 'p': 228, 'q': 229, 'r': 230, 's': 231, 't': 232, 'u': 233, 'v': 234, 'w': 235, 'x': 236, 'y': 237, 'z': 238, '▶': 239, ':': 240, 'Ä': 241, 'Ö': 242, 'Ü': 243, 'ä': 244, 'ö': 245, 'ü': 246, '\\l': 250, '\\p': 251, '\\n': 254, '$': 255, ' ': 0}

CharMap = {}
for key, value in charMap.items():
    CharMap[value] = key

SpecialBuffersReverse = {
	"SUPER_ER": "2C",
	"LV": "34",
	"PK": "53",
	"PKMN": "5354",
	"POKEBLOCK": "5556575859",
	"UP_ARROW": "79",
	"DOWN_ARROW": "7A",
	"LEFT_ARROW": "7B",
	"RIGHT_ARROW": "7C",
	"SUPER_E": "84",
	"SUPER_RE": "A0",
	"TALL_PLUS": "FC0CFB",
	"STRING": "FD",
	"PLAYER": "FD01",
	"STR_VAR_1": "FD02",
	"STR_VAR_2": "FD03",
	"STR_VAR_3": "FD04",
	"KUN": "FD05",
	"RIVAL": "FD06",
	"VERSION": "FD07",
	"EVIL_TEAM": "FD08",
	"GOOD_TEAM": "FD09",
	"EVIL_LEADER": "FD0A",
	"GOOD_LEADER": "FD0B",
	"EVIL_LEGENDARY": "FD0C",
	"GOOD_LEGENDARY": "FD0D",
	"UNKNOWN_STR": "FD00",
	"ATTACKING_TRAINER": "FD08",
	"DEFENDING_TRAINER": "FD09",
	"ATTACKING_MON": "FD0C",
	"DEFENDING_MON": "FD0D",
	"B_BUFF1": "FD00",
	"B_BUFF2": "FD01",
	"B_COPY_VAR_1": "FD02",
	"B_COPY_VAR_2": "FD03",
	"B_COPY_VAR_3": "FD04",
	"B_PLAYER_MON1_NAME": "FD05",
	"B_OPPONENT_MON1_NAME": "FD06",
	"B_PLAYER_MON2_NAME": "FD07",
	"B_OPPONENT_MON2_NAME": "FD08",
	"B_LINK_PLAYER_MON1_NAME": "FD09",
	"B_LINK_OPPONENT_MON1_NAME": "FD0A",
	"B_LINK_PLAYER_MON2_NAME": "FD0B",
	"B_LINK_OPPONENT_MON2_NAME": "FD0C",
	"B_ATK_NAME_WITH_PREFIX_MON1": "FD0D",
	"B_ATK_PARTNER_NAME": "FD0E",
	"B_ATK_NAME_WITH_PREFIX": "FD0F",
	"B_DEF_NAME_WITH_PREFIX": "FD10",
	"B_EFF_NAME_WITH_PREFIX": "FD11",
	"B_ACTIVE_NAME_WITH_PREFIX": "FD12",
	"B_SCR_ACTIVE_NAME_WITH_PREFIX": "FD13",
	"B_CURRENT_MOVE": "FD14",
	"B_LAST_MOVE": "FD15",
	"B_LAST_ITEM": "FD16",
	"B_LAST_ABILITY": "FD17",
	"B_ATK_ABILITY": "FD18",
	"B_DEF_ABILITY": "FD19",
	"B_SCR_ACTIVE_ABILITY": "FD1A",
	"B_EFF_ABILITY": "FD1B",
	"B_TRAINER1_CLASS": "FD1C",
	"B_TRAINER1_NAME": "FD1D",
	"B_LINK_PLAYER_NAME": "FD1E",
	"B_LINK_PARTNER_NAME": "FD1F",
	"B_LINK_OPPONENT1_NAME": "FD20",
	"B_LINK_OPPONENT2_NAME": "FD21",
	"B_LINK_SCR_TRAINER_NAME": "FD22",
	"B_PLAYER_NAME": "FD23",
	"B_TRAINER1_LOSE_TEXT": "FD24",
	"B_TRAINER1_WIN_TEXT": "FD25",
	"B_26": "FD26",
	"B_PC_CREATOR_NAME": "FD27",
	"B_ATK_PREFIX1": "FD28",
	"B_DEF_PREFIX1": "FD29",
	"B_ATK_PREFIX2": "FD2A",
	"B_DEF_PREFIX2": "FD2B",
	"B_ATK_PREFIX3": "FD2C",
	"B_DEF_PREFIX3": "FD2D",
	"B_TRAINER2_LOSE_TEXT": "FD2E",
	"B_TRAINER2_WIN_TEXT": "FD2F",
	"B_BUFF3": "FD30",
	"NAME_END": "FC00",
	"DYNAMIC": "F7",
	"COLOR": "FC01",
	"HIGHLIGHT": "FC02",
	"SHADOW": "FC03",
	"COLOR_HIGHLIGHT_SHADOW": "FC04",
	"PALETTE": "FC05",
	"FONT": "FC06",
	"RESET_FONT": "FC07",
	"PAUSE": "FC08",
	"PAUSE_UNTIL_PRESS": "FC09",
	"WAIT_SE": "FC0A",
	"PLAY_BGM": "FC0B",
	"ESCAPE": "FC0C",
	"SHIFT_RIGHT": "FC0D",
	"SHIFT_DOWN": "FC0E",
	"FILL_WINDOW": "FC0F",
	"PLAY_SE": "FC10",
	"CLEAR": "FC11",
	"SKIP": "FC12",
	"CLEAR_TO": "FC13",
	"MIN_LETTER_SPACING": "FC14",
	"JPN": "FC15",
	"ENG": "FC16",
	"PAUSE_MUSIC": "FC17",
	"RESUME_MUSIC": "FC18",
	"FONT_SMALL": "FC0600",
	"FONT_NORMAL_COPY_1": "FC0601",
	"FONT_NORMAL": "FC0602",
	"FONT_NORMAL_COPY_2": "FC0603",
	"FONT_MALE": "FC0604",
	"FONT_FEMALE": "FC0605",
	"TRANSPARENT": "00",
	"WHITE": "01",
	"DARK_GRAY": "02",
	"LIGHT_GRAY": "03",
	"RED": "04",
	"LIGHT_RED": "05",
	"GREEN": "06",
	"LIGHT_GREEN": "07",
	"BLUE": "08",
	"LIGHT_BLUE": "09",
	"DYNAMIC_COLOR1": "0A",
	"DYNAMIC_COLOR2": "0B",
	"DYNAMIC_COLOR3": "0C",
	"DYNAMIC_COLOR4": "0D",
	"DYNAMIC_COLOR5": "0E",
	"DYNAMIC_COLOR6": "0F",
	"MUS_DUMMY": "0000",
	"SE_USE_ITEM": "0100",
	"SE_PC_LOGIN": "0200",
	"SE_PC_OFF": "0300",
	"SE_PC_ON": "0400",
	"SE_SELECT": "0500",
	"SE_WIN_OPEN": "0600",
	"SE_WALL_HIT": "0700",
	"SE_RS_DOOR": "0800",
	"SE_EXIT": "0900",
	"SE_LEDGE": "0A00",
	"SE_BIKE_BELL": "0B00",
	"SE_NOT_EFFECTIVE": "0C00",
	"SE_EFFECTIVE": "0D00",
	"SE_SUPER_EFFECTIVE": "0E00",
	"SE_BALL_OPEN": "0F00",
	"SE_FAINT": "1000",
	"SE_FLEE": "1100",
	"SE_SLIDING_DOOR": "1200",
	"SE_SHIP": "1300",
	"SE_BANG": "1400",
	"SE_PIN": "1500",
	"SE_BOO": "1600",
	"SE_BALL": "1700",
	"SE_CONTEST_PLACE": "1800",
	"SE_SUCCESS": "1900",
	"SE_FAILURE": "1A00",
	"SE_EXP": "1B00",
	"SE_BIKE_HOP": "1C00",
	"SE_SWITCH": "1D00",
	"SE_CLICK": "1E00",
	"SE_FU_ZAKU": "1F00",
	"SE_CONTEST_CONDITION_LOSE": "2000",
	"SE_LAVARIDGE_FALL_WARP": "2100",
	"SE_ICE_STAIRS": "2200",
	"SE_ICE_BREAK": "2300",
	"SE_ICE_CRACK": "2400",
	"SE_FALL": "2500",
	"SE_UNLOCK": "2600",
	"SE_WARP_IN": "2700",
	"SE_WARP_OUT": "2800",
	"SE_REPEL": "2900",
	"SE_ROTATING_GATE": "2A00",
	"SE_TRUCK_MOVE": "2B00",
	"SE_TRUCK_STOP": "2C00",
	"SE_TRUCK_UNLOAD": "2D00",
	"SE_TRUCK_DOOR": "2E00",
	"SE_BERRY_BLENDER": "2F00",
	"SE_SAVE": "3000",
	"SE_BALL_BOUNCE_1": "3100",
	"SE_BALL_BOUNCE_2": "3200",
	"SE_BALL_BOUNCE_3": "3300",
	"SE_BALL_BOUNCE_4": "3400",
	"SE_BALL_TRADE": "3500",
	"SE_BALL_THROW": "3600",
	"SE_NOTE_C": "3700",
	"SE_NOTE_D": "3800",
	"SE_NOTE_E": "3900",
	"SE_NOTE_F": "3A00",
	"SE_NOTE_G": "3B00",
	"SE_NOTE_A": "3C00",
	"SE_NOTE_B": "3D00",
	"SE_NOTE_C_HIGH": "3E00",
	"SE_PUDDLE": "3F00",
	"SE_BRIDGE_WALK": "4000",
	"SE_ITEMFINDER": "4100",
	"SE_DING_DONG": "4200",
	"SE_BALLOON_RED": "4300",
	"SE_BALLOON_BLUE": "4400",
	"SE_BALLOON_YELLOW": "4500",
	"SE_BREAKABLE_DOOR": "4600",
	"SE_MUD_BALL": "4700",
	"SE_FIELD_POISON": "4800",
	"SE_ESCALATOR": "4900",
	"SE_THUNDERSTORM": "4A00",
	"SE_THUNDERSTORM_STOP": "4B00",
	"SE_DOWNPOUR": "4C00",
	"SE_DOWNPOUR_STOP": "4D00",
	"SE_RAIN": "4E00",
	"SE_RAIN_STOP": "4F00",
	"SE_THUNDER": "5000",
	"SE_THUNDER2": "5100",
	"SE_ELEVATOR": "5200",
	"SE_LOW_HEALTH": "5300",
	"SE_EXP_MAX": "5400",
	"SE_ROULETTE_BALL": "5500",
	"SE_ROULETTE_BALL2": "5600",
	"SE_TAILLOW_WING_FLAP": "5700",
	"SE_RS_SHOP": "5800",
	"SE_CONTEST_HEART": "5900",
	"SE_CONTEST_CURTAIN_RISE": "5A00",
	"SE_CONTEST_CURTAIN_FALL": "5B00",
	"SE_CONTEST_ICON_CHANGE": "5C00",
	"SE_CONTEST_ICON_CLEAR": "5D00",
	"SE_CONTEST_MONS_TURN": "5E00",
	"SE_SHINY": "5F00",
	"SE_INTRO_BLAST": "6000",
	"SE_MUGSHOT": "6100",
	"SE_APPLAUSE": "6200",
	"SE_VEND": "6300",
	"SE_ORB": "6400",
	"SE_DEX_SCROLL": "6500",
	"SE_DEX_PAGE": "6600",
	"SE_POKENAV_ON": "6700",
	"SE_POKENAV_OFF": "6800",
	"SE_DEX_SEARCH": "6900",
	"SE_EGG_HATCH": "6A00",
	"SE_BALL_TRAY_ENTER": "6B00",
	"SE_BALL_TRAY_BALL": "6C00",
	"SE_BALL_TRAY_EXIT": "6D00",
	"SE_GLASS_FLUTE": "6E00",
	"SE_M_THUNDERBOLT": "6F00",
	"SE_M_THUNDERBOLT2": "7000",
	"SE_M_HARDEN": "7100",
	"SE_M_NIGHTMARE": "7200",
	"SE_M_VITAL_THROW": "7300",
	"SE_M_VITAL_THROW2": "7400",
	"SE_M_BUBBLE": "7500",
	"SE_M_BUBBLE2": "7600",
	"SE_M_BUBBLE3": "7700",
	"SE_M_RAIN_DANCE": "7800",
	"SE_M_CUT": "7900",
	"SE_M_STRING_SHOT": "7A00",
	"SE_M_STRING_SHOT2": "7B00",
	"SE_M_ROCK_THROW": "7C00",
	"SE_M_GUST": "7D00",
	"SE_M_GUST2": "7E00",
	"SE_M_DOUBLE_SLAP": "7F00",
	"SE_M_DOUBLE_TEAM": "8000",
	"SE_M_RAZOR_WIND": "8100",
	"SE_M_ICY_WIND": "8200",
	"SE_M_THUNDER_WAVE": "8300",
	"SE_M_COMET_PUNCH": "8400",
	"SE_M_MEGA_KICK": "8500",
	"SE_M_MEGA_KICK2": "8600",
	"SE_M_CRABHAMMER": "8700",
	"SE_M_JUMP_KICK": "8800",
	"SE_M_FLAME_WHEEL": "8900",
	"SE_M_FLAME_WHEEL2": "8A00",
	"SE_M_FLAMETHROWER": "8B00",
	"SE_M_FIRE_PUNCH": "8C00",
	"SE_M_TOXIC": "8D00",
	"SE_M_SACRED_FIRE": "8E00",
	"SE_M_SACRED_FIRE2": "8F00",
	"SE_M_EMBER": "9000",
	"SE_M_TAKE_DOWN": "9100",
	"SE_M_BLIZZARD": "9200",
	"SE_M_BLIZZARD2": "9300",
	"SE_M_SCRATCH": "9400",
	"SE_M_VICEGRIP": "9500",
	"SE_M_WING_ATTACK": "9600",
	"SE_M_FLY": "9700",
	"SE_M_SAND_ATTACK": "9800",
	"SE_M_RAZOR_WIND2": "9900",
	"SE_M_BITE": "9A00",
	"SE_M_HEADBUTT": "9B00",
	"SE_M_SURF": "9C00",
	"SE_M_HYDRO_PUMP": "9D00",
	"SE_M_WHIRLPOOL": "9E00",
	"SE_M_HORN_ATTACK": "9F00",
	"SE_M_TAIL_WHIP": "A000",
	"SE_M_MIST": "A100",
	"SE_M_POISON_POWDER": "A200",
	"SE_M_BIND": "A300",
	"SE_M_DRAGON_RAGE": "A400",
	"SE_M_SING": "A500",
	"SE_M_PERISH_SONG": "A600",
	"SE_M_PAY_DAY": "A700",
	"SE_M_DIG": "A800",
	"SE_M_DIZZY_PUNCH": "A900",
	"SE_M_SELF_DESTRUCT": "AA00",
	"SE_M_EXPLOSION": "AB00",
	"SE_M_ABSORB_2": "AC00",
	"SE_M_ABSORB": "AD00",
	"SE_M_SCREECH": "AE00",
	"SE_M_BUBBLE_BEAM": "AF00",
	"SE_M_BUBBLE_BEAM2": "B000",
	"SE_M_SUPERSONIC": "B100",
	"SE_M_BELLY_DRUM": "B200",
	"SE_M_METRONOME": "B300",
	"SE_M_BONEMERANG": "B400",
	"SE_M_LICK": "B500",
	"SE_M_PSYBEAM": "B600",
	"SE_M_FAINT_ATTACK": "B700",
	"SE_M_SWORDS_DANCE": "B800",
	"SE_M_LEER": "B900",
	"SE_M_SWAGGER": "BA00",
	"SE_M_SWAGGER2": "BB00",
	"SE_M_HEAL_BELL": "BC00",
	"SE_M_CONFUSE_RAY": "BD00",
	"SE_M_SNORE": "BE00",
	"SE_M_BRICK_BREAK": "BF00",
	"SE_M_GIGA_DRAIN": "C000",
	"SE_M_PSYBEAM2": "C100",
	"SE_M_SOLAR_BEAM": "C200",
	"SE_M_PETAL_DANCE": "C300",
	"SE_M_TELEPORT": "C400",
	"SE_M_MINIMIZE": "C500",
	"SE_M_SKETCH": "C600",
	"SE_M_SWIFT": "C700",
	"SE_M_REFLECT": "C800",
	"SE_M_BARRIER": "C900",
	"SE_M_DETECT": "CA00",
	"SE_M_LOCK_ON": "CB00",
	"SE_M_MOONLIGHT": "CC00",
	"SE_M_CHARM": "CD00",
	"SE_M_CHARGE": "CE00",
	"SE_M_STRENGTH": "CF00",
	"SE_M_HYPER_BEAM": "D000",
	"SE_M_WATERFALL": "D100",
	"SE_M_REVERSAL": "D200",
	"SE_M_ACID_ARMOR": "D300",
	"SE_M_SANDSTORM": "D400",
	"SE_M_TRI_ATTACK": "D500",
	"SE_M_TRI_ATTACK2": "D600",
	"SE_M_ENCORE": "D700",
	"SE_M_ENCORE2": "D800",
	"SE_M_BATON_PASS": "D900",
	"SE_M_MILK_DRINK": "DA00",
	"SE_M_ATTRACT": "DB00",
	"SE_M_ATTRACT2": "DC00",
	"SE_M_MORNING_SUN": "DD00",
	"SE_M_FLATTER": "DE00",
	"SE_M_SAND_TOMB": "DF00",
	"SE_M_GRASSWHISTLE": "E000",
	"SE_M_SPIT_UP": "E100",
	"SE_M_DIVE": "E200",
	"SE_M_EARTHQUAKE": "E300",
	"SE_M_TWISTER": "E400",
	"SE_M_SWEET_SCENT": "E500",
	"SE_M_YAWN": "E600",
	"SE_M_SKY_UPPERCUT": "E700",
	"SE_M_STAT_INCREASE": "E800",
	"SE_M_HEAT_WAVE": "E900",
	"SE_M_UPROAR": "EA00",
	"SE_M_HAIL": "EB00",
	"SE_M_COSMIC_POWER": "EC00",
	"SE_M_TEETER_DANCE": "ED00",
	"SE_M_STAT_DECREASE": "EE00",
	"SE_M_HAZE": "EF00",
	"SE_M_HYPER_BEAM2": "F000",
	"SE_DOOR": "F100",
	"SE_CARD_FLIP": "F200",
	"SE_CARD_FLIPPING": "F300",
	"SE_CARD_OPEN": "F400",
	"SE_BAG_CURSOR": "F500",
	"SE_BAG_POCKET": "F600",
	"SE_BALL_CLICK": "F700",
	"SE_SHOP": "F800",
	"SE_SS_ANNE_HORN": "F900",
	"SE_HELP_OPEN": "FA00",
	"SE_HELP_CLOSE": "FB00",
	"SE_HELP_ERROR": "FC00",
	"SE_DEOXYS_MOVE": "FD00",
	"SE_POKE_JUMP_SUCCESS": "FE00",
	"SE_POKE_JUMP_FAILURE": "FF00",
	"MUS_HEAL": "0001",
	"MUS_LEVEL_UP": "0101",
	"MUS_OBTAIN_ITEM": "0201",
	"MUS_EVOLVED": "0301",
	"MUS_OBTAIN_BADGE": "0401",
	"MUS_OBTAIN_TMHM": "0501",
	"MUS_OBTAIN_BERRY": "0601",
	"MUS_EVOLUTION_INTRO": "0701",
	"MUS_EVOLUTION": "0801",
	"MUS_RS_VS_GYM_LEADER": "0901",
	"MUS_RS_VS_TRAINER": "0A01",
	"MUS_SCHOOL": "0B01",
	"MUS_SLOTS_JACKPOT": "0C01",
	"MUS_SLOTS_WIN": "0D01",
	"MUS_MOVE_DELETED": "0E01",
	"MUS_TOO_BAD": "0F01",
	"MUS_FOLLOW_ME": "1001",
	"MUS_GAME_CORNER": "1101",
	"MUS_ROCKET_HIDEOUT": "1201",
	"MUS_GYM": "1301",
	"MUS_JIGGLYPUFF": "1401",
	"MUS_INTRO_FIGHT": "1501",
	"MUS_TITLE": "1601",
	"MUS_CINNABAR": "1701",
	"MUS_LAVENDER": "1801",
	"MUS_HEAL_UNUSED": "1901",
	"MUS_CYCLING": "1A01",
	"MUS_ENCOUNTER_ROCKET": "1B01",
	"MUS_ENCOUNTER_GIRL": "1C01",
	"MUS_ENCOUNTER_BOY": "1D01",
	"MUS_HALL_OF_FAME": "1E01",
	"MUS_VIRIDIAN_FOREST": "1F01",
	"MUS_MT_MOON": "2001",
	"MUS_POKE_MANSION": "2101",
	"MUS_CREDITS": "2201",
	"MUS_ROUTE1": "2301",
	"MUS_ROUTE24": "2401",
	"MUS_ROUTE3": "2501",
	"MUS_ROUTE11": "2601",
	"MUS_VICTORY_ROAD": "2701",
	"MUS_VS_GYM_LEADER": "2801",
	"MUS_VS_TRAINER": "2901",
	"MUS_VS_WILD": "2A01",
	"MUS_VS_CHAMPION": "2B01",
	"MUS_PALLET": "2C01",
	"MUS_OAK_LAB": "2D01",
	"MUS_OAK": "2E01",
	"MUS_POKE_CENTER": "2F01",
	"MUS_SS_ANNE": "3001",
	"MUS_SURF": "3101",
	"MUS_POKE_TOWER": "3201",
	"MUS_SILPH": "3301",
	"MUS_FUCHSIA": "3401",
	"MUS_CELADON": "3501",
	"MUS_VICTORY_TRAINER": "3601",
	"MUS_VICTORY_WILD": "3701",
	"MUS_VICTORY_GYM_LEADER": "3801",
	"MUS_VERMILLION": "3901",
	"MUS_PEWTER": "3A01",
	"MUS_ENCOUNTER_RIVAL": "3B01",
	"MUS_RIVAL_EXIT": "3C01",
	"MUS_DEX_RATING": "3D01",
	"MUS_OBTAIN_KEY_ITEM": "3E01",
	"MUS_CAUGHT_INTRO": "3F01",
	"MUS_PHOTO": "4001",
	"MUS_GAME_FREAK": "4101",
	"MUS_CAUGHT": "4201",
	"MUS_NEW_GAME_INSTRUCT": "4301",
	"MUS_NEW_GAME_INTRO": "4401",
	"MUS_NEW_GAME_EXIT": "4501",
	"MUS_POKE_JUMP": "4601",
	"MUS_UNION_ROOM": "4701",
	"MUS_NET_CENTER": "4801",
	"MUS_MYSTERY_GIFT": "4901",
	"MUS_BERRY_PICK": "4A01",
	"MUS_SEVII_CAVE": "4B01",
	"MUS_TEACHY_TV_SHOW": "4C01",
	"MUS_SEVII_ROUTE": "4D01",
	"MUS_SEVII_DUNGEON": "4E01",
	"MUS_SEVII_123": "4F01",
	"MUS_SEVII_45": "5001",
	"MUS_SEVII_67": "5101",
	"MUS_POKE_FLUTE": "5201",
	"MUS_VS_DEOXYS": "5301",
	"MUS_VS_MEWTWO": "5401",
	"MUS_VS_LEGEND": "5501",
	"MUS_ENCOUNTER_GYM_LEADER": "5601",
	"MUS_ENCOUNTER_DEOXYS": "5701",
	"MUS_TRAINER_TOWER": "5801",
	"MUS_SLOW_PALLET": "5901",
	"MUS_TEACHY_TV_MENU": "5A01",
	"A_BUTTON": "F800",
	"B_BUTTON": "F801",
	"L_BUTTON": "F802",
	"R_BUTTON": "F803",
	"START_BUTTON": "F804",
	"SELECT_BUTTON": "F805",
	"DPAD_UP": "F806",
	"DPAD_DOWN": "F807",
	"DPAD_LEFT": "F808",
	"DPAD_RIGHT": "F809",
	"DPAD_UPDOWN": "F80A",
	"DPAD_LEFTRIGHT": "F80B",
	"DPAD_ANY": "F80C",
	"UP_ARROW_2": "F900",
	"DOWN_ARROW_2": "F901",
	"LEFT_ARROW_2": "F902",
	"RIGHT_ARROW_2": "F903",
	"PLUS": "F904",
	"LV_2": "F905",
	"PP": "F906",
	"ID": "F907",
	"NO": "F908",
	"UNDERSCORE": "F909",
	"CIRCLE_1": "F90A",
	"CIRCLE_2": "F90B",
	"CIRCLE_3": "F90C",
	"CIRCLE_4": "F90D",
	"CIRCLE_5": "F90E",
	"CIRCLE_6": "F90F",
	"CIRCLE_7": "F910",
	"CIRCLE_8": "F911",
	"CIRCLE_9": "F912",
	"LEFT_PAREN": "F913",
	"RIGHT_PAREN": "F914",
	"CIRCLE_DOT": "F915",
	"TRIANGLE": "F916",
	"BIG_MULT_X": "F917",
	"EMOJI_UNDERSCORE": "F9D0",
	"EMOJI_PIPE": "F9D1",
	"EMOJI_HIGHBAR": "F9D2",
	"EMOJI_TILDE": "F9D3",
	"EMOJI_LEFT_PAREN": "F9D4",
	"EMOJI_RIGHT_PAREN": "F9D5",
	"EMOJI_UNION": "F9D6",
	"EMOJI_GREATER_THAN": "F9D7",
	"EMOJI_LEFT_EYE": "F9D8",
	"EMOJI_RIGHT_EYE": "F9D9",
	"EMOJI_AT": "F9DA",
	"EMOJI_SEMICOLON": "F9DB",
	"EMOJI_PLUS": "F9DC",
	"EMOJI_MINUS": "F9DD",
	"EMOJI_EQUALS": "F9DE",
	"EMOJI_SPIRAL": "F9DF",
	"EMOJI_TONGUE": "F9E0",
	"EMOJI_TRIANGLE_OUTLINE": "F9E1",
	"EMOJI_ACUTE": "F9E2",
	"EMOJI_GRAVE": "F9E3",
	"EMOJI_CIRCLE": "F9E4",
	"EMOJI_TRIANGLE": "F9E5",
	"EMOJI_SQUARE": "F9E6",
	"EMOJI_HEART": "F9E7",
	"EMOJI_MOON": "F9E8",
	"EMOJI_NOTE": "F9E9",
	"EMOJI_BALL": "F9EA",
	"EMOJI_BOLT": "F9EB",
	"EMOJI_LEAF": "F9EC",
	"EMOJI_FIRE": "F9ED",
	"EMOJI_WATER": "F9EE",
	"EMOJI_LEFT_FIST": "F9EF",
	"EMOJI_RIGHT_FIST": "F9F0",
	"EMOJI_BIGWHEEL": "F9F1",
	"EMOJI_SMALLWHEEL": "F9F2",
	"EMOJI_SPHERE": "F9F3",
	"EMOJI_IRRITATED": "F9F4",
	"EMOJI_MISCHIEVOUS": "F9F5",
	"EMOJI_HAPPY": "F9F6",
	"EMOJI_ANGRY": "F9F7",
	"EMOJI_SURPRISED": "F9F8",
	"EMOJI_BIGSMILE": "F9F9",
	"EMOJI_EVIL": "F9FA",
	"EMOJI_TIRED": "F9FB",
	"EMOJI_NEUTRAL": "F9FC",
	"EMOJI_SHOCKED": "F9FD",
	"EMOJI_BIGANGER": "F9FE",
}

SpecialBuffers = {}
for key, value in SpecialBuffersReverse.items():
    SpecialBuffers[value] = key

f = open("output.txt", "w")

from deep_translator import GoogleTranslator
from time import sleep
from tqdm import tqdm
num3 = 0
nineWidths = ['PLAYER', 'RIVAL', 'STR_VAR_1', 'STR_VAR_2', 'STR_VAR_3', 'B_BUFF2', 'B_OPPONENT_MON1_NAME', 'B_COPY_VAR_1', 'B_COPY_VAR_2', 'B_COPY_VAR_3']
SOURCE_ROM = "BPRE0.gba"
with open(SOURCE_ROM, 'rb+') as rom:
    for symbol_index in tqdm(range(len(pokefirered_sym))):
        symbol = pokefirered_sym[symbol_index]
        string = symbol[3]
        offset = symbol[0][2:]
        offset_actual = symbol[0]
        # if string == '#org @sText_PkmnClamped':
        if int('0x' + offset_actual, 16) >= int('0x08000000', 16):
            widths = {}
            width = 39
            widthNum = 0
            if string in TextScripts:
                constructedString = ''
                rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                ordROM = ord(rom.read(1))
                num = 0
                num2 = 0
                try:
                    while ordROM != 255:
                        if ordROM in CharMap:
                            num2 = 0
                            if num > -1:
                                constructedString += CharMap[ordROM]
                            num = num + 1
                            offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM2 = rom.read(2)
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000 - 2)
                            ordROM3 = rom.read(3)
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000 - 3)
                            ordROM5 = rom.read(5)
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000 - 5)
                            ordROM_2 = ''
                            ordROM_3 = ''
                            ordROM_5 = ''
                            for ordROM2_1 in list(ordROM2):
                                if ordROM2_1 < 16:
                                    ordROM_2 += '0' + str(hex(ordROM2_1)).replace('0x', '').upper()
                                else:
                                    ordROM_2 += str(hex(ordROM2_1)).replace('0x', '').upper()
                            for ordROM3_1 in list(ordROM3):
                                if ordROM3_1 < 16:
                                    ordROM_3 += '0' + str(hex(ordROM3_1)).replace('0x', '').upper()
                                else:
                                    ordROM_3 += str(hex(ordROM3_1)).replace('0x', '').upper()
                            for ordROM5_1 in list(ordROM5):
                                if ordROM5_1 < 16:
                                    ordROM_5 += '0' + str(hex(ordROM5_1)).replace('0x', '').upper()
                                else:
                                    ordROM_5 += str(hex(ordROM5_1)).replace('0x', '').upper()
                            if num2 > -1:
                                if ordROM_2 in SpecialBuffers:
                                    constructedString += '[' + SpecialBuffers[ordROM_2] + ']'
                                elif ordROM_3 in SpecialBuffers:
                                    constructedString += '[' + SpecialBuffers[ordROM_3] + ']'
                                elif ordROM_5 in SpecialBuffers:
                                    constructedString += '[' + SpecialBuffers[ordROM_5] + ']'
                            num2 = num2 + 1
                            offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                except:
                    pass
                if constructedString and constructedString[-1] == '$':
                    text = constructedString[:-1]
                    text_newline = text.replace('\n', '\\n')
                    translated_text = ''
                    if '[' in text:
                        splitted_text = text_newline.split('[')
                        for splitted_text_section in splitted_text:
                            if ']' in splitted_text_section:
                                splitted_text_2 = splitted_text_section.split(']')
                                for splitted_text_section_2 in splitted_text_2:
                                    if splitted_text_section_2 not in SpecialBuffers:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                            if splitted_text_3 not in SpecialBuffers and splitted_text_4 not in SpecialBuffers:
                                                try:
                                                    translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                                except:
                                                    pass
                                                width = 39
                                                widths[widthNum] = width
                                                widthNum = widthNum + 1
                                            else:
                                                translated_text += '[' + splitted_text_section_2 + ']'
                                                if splitted_text_section_2 in nineWidths:
                                                    width = 48
                                                else:
                                                    width = 39
                                                widths[widthNum] = width
                                                widthNum = widthNum + 1
                                        else:
                                            translated_text += '[' + splitted_text_section_2 + ']'
                                            if splitted_text_section_2 in nineWidths:
                                                width = 48
                                            else:
                                                width = 39
                                            widths[widthNum] = width
                                            widthNum = widthNum + 1
                                    else:
                                        translated_text += '[' + splitted_text_section_2 + ']'
                                        if splitted_text_section_2 in nineWidths:
                                            width = 48
                                        else:
                                            width = 39
                                        widths[widthNum] = width
                                        widthNum = widthNum + 1
                    if translated_text != '':
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                elif width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
                    else:
                        translated_text = GoogleTranslator(source='auto', target='es').translate(text_newline)
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
                elif constructedString and constructedString[-1] != '$':
                    text = constructedString
                    text_newline = text.replace('\n', '\\n')
                    translated_text = ''
                    if '[' in text:
                        splitted_text = text_newline.split('[')
                        for splitted_text_section in splitted_text:
                            if ']' in splitted_text_section:
                                splitted_text_2 = splitted_text_section.split(']')
                                for splitted_text_section_2 in splitted_text_2:
                                    if splitted_text_section_2 not in SpecialBuffers:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                            if splitted_text_3 not in SpecialBuffers and splitted_text_4 not in SpecialBuffers:
                                                try:
                                                    translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                                except:
                                                    pass
                                                width = 39
                                                widths[widthNum] = width
                                                widthNum = widthNum + 1
                                            else:
                                                translated_text += '[' + splitted_text_section_2 + ']'
                                                if splitted_text_section_2 in nineWidths:
                                                    width = 48
                                                else:
                                                    width = 39
                                                widths[widthNum] = width
                                                widthNum = widthNum + 1
                                        else:
                                            translated_text += '[' + splitted_text_section_2 + ']'
                                            if splitted_text_section_2 in nineWidths:
                                                width = 48
                                            else:
                                                width = 39
                                            widths[widthNum] = width
                                            widthNum = widthNum + 1
                                    else:
                                        translated_text += '[' + splitted_text_section_2 + ']'
                                        if splitted_text_section_2 in nineWidths:
                                            width = 48
                                        else:
                                            width = 39
                                        widths[widthNum] = width
                                        widthNum = widthNum + 1
                    if translated_text != '':
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
                    else:
                        translated_text = GoogleTranslator(source='auto', target='es').translate(text_newline)
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
            elif string in JapaneseTextScripts:
                constructedString = ''
                rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                ordROM = ord(rom.read(1))
                num = 0
                num2 = 0
                try:
                    while ordROM != 255:
                        if ordROM < 16:
                            returnValue = '0' + hex(ordROM).replace('0x', '').upper()
                        else:
                            returnValue = hex(ordROM).replace('0x', '').upper()
                        if returnValue in Japanese:
                            num2 = 0
                            if num > -1:
                                constructedString += Japanese[returnValue]
                            num = num + 1
                            offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM2 = rom.read(2)
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000 - 2)
                            ordROM3 = rom.read(3)
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000 - 3)
                            ordROM5 = rom.read(5)
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000 - 5)
                            ordROM_2 = ''
                            ordROM_3 = ''
                            ordROM_5 = ''
                            for ordROM2_1 in list(ordROM2):
                                if ordROM2_1 < 16:
                                    ordROM_2 += '0' + str(hex(ordROM2_1)).replace('0x', '').upper()
                                else:
                                    ordROM_2 += str(hex(ordROM2_1)).replace('0x', '').upper()
                            for ordROM3_1 in list(ordROM3):
                                if ordROM3_1 < 16:
                                    ordROM_3 += '0' + str(hex(ordROM3_1)).replace('0x', '').upper()
                                else:
                                    ordROM_3 += str(hex(ordROM3_1)).replace('0x', '').upper()
                            for ordROM5_1 in list(ordROM5):
                                if ordROM5_1 < 16:
                                    ordROM_5 += '0' + str(hex(ordROM5_1)).replace('0x', '').upper()
                                else:
                                    ordROM_5 += str(hex(ordROM5_1)).replace('0x', '').upper()
                            if num2 > -1:
                                if ordROM_2 in SpecialBuffers:
                                    constructedString += '[' + SpecialBuffers[ordROM_2] + ']'
                                elif ordROM_3 in SpecialBuffers:
                                    constructedString += '[' + SpecialBuffers[ordROM_3] + ']'
                                elif ordROM_5 in SpecialBuffers:
                                    constructedString += '[' + SpecialBuffers[ordROM_5] + ']'
                            num2 = num2 + 1
                            offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                except:
                    pass
                if constructedString and constructedString[-1] == '$':
                    text = constructedString[:-1]
                    text_newline = text.replace('\n', '\\n')
                    translated_text = ''
                    if '{' in text:
                        splitted_text = text_newline.split('{')
                        for splitted_text_section in splitted_text:
                            if '}' in splitted_text_section:
                                splitted_text_2 = splitted_text_section.split('}')
                                for splitted_text_section_2 in splitted_text_2:
                                    if splitted_text_section_2 not in SpecialBuffers:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                        if splitted_text_3 not in SpecialBuffers and splitted_text_4 not in SpecialBuffers:
                                            try:
                                                translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                            except:
                                                pass
                                        else:
                                            translated_text += '{' + splitted_text_section_2 + '}'
                                    else:
                                        translated_text += '{' + splitted_text_section_2 + '}'
                    if translated_text != '':
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
                    else:
                        translated_text = GoogleTranslator(source='auto', target='es').translate(text_newline)
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
                elif constructedString and constructedString[-1] != '$':
                    text = constructedString
                    text_newline = text.replace('\n', '\\n')
                    translated_text = ''
                    if '{' in text:
                        splitted_text = text_newline.split('{')
                        for splitted_text_section in splitted_text:
                            if '}' in splitted_text_section:
                                splitted_text_2 = splitted_text_section.split('}')
                                for splitted_text_section_2 in splitted_text_2:
                                    if splitted_text_section_2 not in SpecialBuffers:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                        if splitted_text_3 not in SpecialBuffers and splitted_text_4 not in SpecialBuffers:
                                            try:
                                                translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                            except:
                                                pass
                                        else:
                                            translated_text += '{' + splitted_text_section_2 + '}'
                                    else:
                                        translated_text += '{' + splitted_text_section_2 + '}'
                    if translated_text != '':
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
                    else:
                        translated_text = GoogleTranslator(source='auto', target='es').translate(text_newline)
                        line_endings = 'npl'
                        line_endings_store = ''
                        pos = 0
                        try:
                            for char in translated_text:
                                if char == '\\':
                                    try:
                                        if translated_text[pos + 1] in line_endings:
                                            line_endings_store = line_endings_store + translated_text[pos + 1]
                                    except:
                                        pass
                                pos = pos + 1
                            sanitizedText = translated_text.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')
                            wrapped_text = ''
                            numWidth = 0
                            width_ = 0
                            actualWidth = 0
                            limit = 39
                            count = 0
                            charIndex = 0
                            while charIndex < len(sanitizedText):
                                char = sanitizedText[charIndex]
                                wrapped_text = wrapped_text + char
                                width_ = width_ + 1
                                if width_ >= limit and count % 2 == 0 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\n'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if width_ >= limit and count % 2 == 1 and char == ' ':
                                    wrapped_text = wrapped_text[:-1] + '\\p'
                                    width_ = 0
                                    limit = 39
                                    count = count + 1
                                if char == '[':
                                    stringStore = sanitizedText[charIndex + 1:].split(']')[0]
                                    wrapped_text = wrapped_text + stringStore + ']'
                                    if stringStore in nineWidths:
                                        limit = limit + len(stringStore) + 11
                                        charIndex = charIndex + len(stringStore) + 1
                                    else:
                                        limit = limit + len(stringStore) + 2
                                        charIndex = charIndex + len(stringStore) + 1
                                charIndex = charIndex + 1
                            f.write('#org @' + string + '\n' + wrapped_text + '\n')
                        except:
                            pass
f.close()