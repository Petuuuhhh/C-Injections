import TextScripts
from TextScripts import TextScripts, pokefirered_sym, charMap, CharMap, SpecialBuffersReverse, SpecialBuffers
from Japanese import JapaneseChars, Japanese
from deep_translator import GoogleTranslator
from time import sleep
from tqdm import tqdm
from langdetect import detect_langs

nineWidths = ['B_BUFF2', 'B_OPPONENT_MON1_NAME', 'B_COPY_VAR_1', 'B_COPY_VAR_2', 'B_COPY_VAR_3']
SOURCE_ROM = "BPRE0.gba"
num3 = 0

f = open("output.txt", "w")
with open(SOURCE_ROM, 'rb+') as rom:
    for symbol_index in tqdm(range(len(pokefirered_sym))):
        symbol = pokefirered_sym[symbol_index]
        string = symbol[3]
        offset = symbol[0][2:]
        offset_actual = symbol[0]
        rom_offset = offset_actual
        # if string == 'PokemonLeague_LoreleisRoom_Text_Intro':
        if int('0x' + offset_actual, 16) >= int('0x08000000', 16):
            if string in TextScripts:
                constructedString = ''
                constructedString2 = ''
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
                rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                ordROM = ord(rom.read(1))
                num = 0
                num2 = 0
                try:
                    while ordROM != 255:
                        global returnValue
                        if ordROM < 16:
                            returnValue = '0' + hex(ordROM).replace('0x', '').upper()
                        else:
                            returnValue = hex(ordROM).replace('0x', '').upper()
                        if returnValue in Japanese:
                            num2 = 0
                            if num > -1:
                                constructedString2 += Japanese[returnValue]
                            num = num + 1
                            rom_offset = hex(int(rom_offset, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM2 = rom.read(2)
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000 - 2)
                            ordROM3 = rom.read(3)
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000 - 3)
                            ordROM5 = rom.read(5)
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000 - 5)
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
                                    constructedString2 += '[' + SpecialBuffers[ordROM_2] + ']'
                                elif ordROM_3 in SpecialBuffers:
                                    constructedString2 += '[' + SpecialBuffers[ordROM_3] + ']'
                                elif ordROM_5 in SpecialBuffers:
                                    constructedString2 += '[' + SpecialBuffers[ordROM_5] + ']'
                            num2 = num2 + 1
                            rom_offset = hex(int(rom_offset, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                except:
                    pass
                langs = {}
                langs2 = {}
                try:
                    for lang in detect_langs(constructedString):
                        langs[str(lang).split(':')[0]] = str(lang).split(':')[1]
                    for lang in detect_langs(constructedString2):
                        langs2[str(lang).split(':')[0]] = str(lang).split(':')[1]
                    if 'en' not in langs and 'ja' in langs2:
                        english = GoogleTranslator(source='auto', target='en').translate(constructedString2)
                        constructedString = english
                except:
                    constructedString = constructedString
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
                                            elif splitted_text_section_2 in SpecialBuffers:
                                                if constructedString.split('[')[0] == '':
                                                    translated_text += '[' + splitted_text_section_2 + '] '
                                                elif constructedString.split(']')[0] == '':
                                                    translated_text += ' [' + splitted_text_section_2 + ']'
                                                else:
                                                    translated_text += ' [' + splitted_text_section_2 + '] '
                                        elif splitted_text_section_2 in SpecialBuffers:
                                            if constructedString.split('[')[0] == '':
                                                translated_text += '[' + splitted_text_section_2 + '] '
                                            elif constructedString.split(']')[0] == '':
                                                translated_text += ' [' + splitted_text_section_2 + ']'
                                            else:
                                                translated_text += ' [' + splitted_text_section_2 + '] '
                                    elif splitted_text_section_2 in SpecialBuffers:
                                        if constructedString.split('[')[0] == '':
                                            translated_text += '[' + splitted_text_section_2 + '] '
                                        elif constructedString.split(']')[0] == '':
                                            translated_text += ' [' + splitted_text_section_2 + ']'
                                        else:
                                            translated_text += ' [' + splitted_text_section_2 + '] '
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
                            f.write('#org @' + string + '\n' + wrapped_text + '\n\n')
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
                            f.write('#org @' + string + '\n' + wrapped_text + '\n\n')
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
                                            elif splitted_text_section_2 in SpecialBuffers:
                                                if constructedString.split('[')[0] == '':
                                                    translated_text += '[' + splitted_text_section_2 + '] '
                                                elif constructedString.split(']')[0] == '':
                                                    translated_text += ' [' + splitted_text_section_2 + ']'
                                                else:
                                                    translated_text += ' [' + splitted_text_section_2 + '] '
                                        elif splitted_text_section_2 in SpecialBuffers:
                                            if constructedString.split('[')[0] == '':
                                                translated_text += '[' + splitted_text_section_2 + '] '
                                            elif constructedString.split(']')[0] == '':
                                                translated_text += ' [' + splitted_text_section_2 + ']'
                                            else:
                                                translated_text += ' [' + splitted_text_section_2 + '] '
                                    elif splitted_text_section_2 in SpecialBuffers:
                                        if constructedString.split('[')[0] == '':
                                            translated_text += '[' + splitted_text_section_2 + '] '
                                        elif constructedString.split(']')[0] == '':
                                            translated_text += ' [' + splitted_text_section_2 + ']'
                                        else:
                                            translated_text += ' [' + splitted_text_section_2 + '] '
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
                            f.write('#org @' + string + '\n' + wrapped_text + '\n\n')
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
                            f.write('#org @' + string + '\n' + wrapped_text + '\n\n')
                        except:
                            pass
f.close()