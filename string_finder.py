import TextScripts
from TextScripts import TextScripts, pokefirered_sym, charMap, CharMap, SpecialBuffersReverse, SpecialBuffers
from Japanese import JapaneseChars, Japanese
import re
from deep_translator import GoogleTranslator
from langdetect import detect_langs
# from tqdm import tqdm

nineWidths = ['B_BUFF2', 'B_OPPONENT_MON1_NAME', 'B_COPY_VAR_1', 'B_COPY_VAR_2', 'B_COPY_VAR_3']
SOURCE_ROM = "BPRE0.gba"
num3 = 0

f = open("output.txt", "w")
with open(SOURCE_ROM, 'rb+') as rom:
    for symbol_index in range(len(pokefirered_sym)):
        symbol = pokefirered_sym[symbol_index]
        string = symbol[3]
        offset = symbol[0][2:]
        offset_actual = symbol[0]
        rom_offset = offset_actual
        # if string == 'Help_Text_HowToEnterName':
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
                        if ordROM in CharMap and ordROM_2 not in SpecialBuffers and ordROM_3 not in SpecialBuffers and ordROM_5 not in SpecialBuffers:
                            num2 = 0
                            if num > -1:
                                constructedString += CharMap[ordROM]
                            num = num + 1
                            offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            if num2 > -1:
                                if ordROM_2 in SpecialBuffers:
                                    # print(2, SpecialBuffers[ordROM_2])
                                    constructedString += '[' + SpecialBuffers[ordROM_2] + ']'
                                    offset_actual = hex(int(offset_actual, 16) + int('02', 16)).replace('0x', '')
                                elif ordROM_3 in SpecialBuffers:
                                    # print(3, SpecialBuffers[ordROM_3])
                                    constructedString += '[' + SpecialBuffers[ordROM_3] + ']'
                                    offset_actual = hex(int(offset_actual, 16) + int('03', 16)).replace('0x', '')
                                elif ordROM_5 in SpecialBuffers:
                                    # print(5, SpecialBuffers[ordROM_5])
                                    constructedString += '[' + SpecialBuffers[ordROM_5] + ']'
                                    offset_actual = hex(int(offset_actual, 16) + int('05', 16)).replace('0x', '')
                                else:
                                    offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            num2 = num2 + 1
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
                        if returnValue in Japanese and ordROM_2 not in SpecialBuffers and ordROM_3 not in SpecialBuffers and ordROM_5 not in SpecialBuffers:
                            num2 = 0
                            if num > -1:
                                constructedString2 += Japanese[returnValue]
                            num = num + 1
                            rom_offset = hex(int(rom_offset, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            if num2 > -1:
                                if ordROM_2 in SpecialBuffers:
                                    # print(2, SpecialBuffers[ordROM_2])
                                    constructedString2 += '[' + SpecialBuffers[ordROM_2] + ']'
                                    rom_offset = hex(int(rom_offset, 16) + int('02', 16)).replace('0x', '')
                                elif ordROM_3 in SpecialBuffers:
                                    # print(3, SpecialBuffers[ordROM_3])
                                    constructedString2 += '[' + SpecialBuffers[ordROM_3] + ']'
                                    rom_offset = hex(int(rom_offset, 16) + int('03', 16)).replace('0x', '')
                                elif ordROM_5 in SpecialBuffers:
                                    # print(5, SpecialBuffers[ordROM_5])
                                    constructedString2 += '[' + SpecialBuffers[ordROM_5] + ']'
                                    rom_offset = hex(int(rom_offset, 16) + int('05', 16)).replace('0x', '')
                                else:
                                    rom_offset = hex(int(rom_offset, 16) + int('01', 16)).replace('0x', '')
                            num2 = num2 + 1
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                except:
                    pass
                langs = {}
                langs2 = {}
                translated_text = ''
                try:
                    for lang in detect_langs(constructedString):
                        langs[str(lang).split(':')[0]] = str(lang).split(':')[1]
                    for lang in detect_langs(constructedString2):
                        langs2[str(lang).split(':')[0]] = str(lang).split(':')[1]
                    if 'en' not in langs and 'ja' in langs2:
                        constructedString = constructedString2
                        if '[' in constructedString:
                            splitted_text = constructedString.split('[')
                            for splitted_text_section in splitted_text:
                                if ']' in splitted_text_section:
                                    splitted_text_2 = splitted_text_section.split(']')
                                    for splitted_text_section_2 in splitted_text_2:
                                        if splitted_text_section_2 not in SpecialBuffersReverse:
                                            if ' ' in splitted_text_section_2:
                                                splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                                splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                                if splitted_text_3 not in SpecialBuffersReverse and splitted_text_4 not in SpecialBuffersReverse:
                                                    try:
                                                        translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                                    except:
                                                        pass
                                                elif splitted_text_3 in SpecialBuffersReverse:
                                                    if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                        translated_text += '[' + splitted_text_3 + '] '
                                                    elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                        translated_text += ' [' + splitted_text_3 + ']'
                                                    elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                        translated_text += ' [' + splitted_text_3 + '] '
                                                    else:
                                                        translated_text += '[' + splitted_text_3 + ']'
                                                elif splitted_text_4 in SpecialBuffersReverse:
                                                    if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                        translated_text += '[' + splitted_text_4 + '] '
                                                    elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                        translated_text += ' [' + splitted_text_4 + ']'
                                                    elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                        translated_text += ' [' + splitted_text_4 + '] '
                                                    else:
                                                        translated_text += '[' + splitted_text_3 + ']'
                                        elif splitted_text_section_2 in SpecialBuffersReverse:
                                            if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                translated_text += '[' + splitted_text_section_2 + '] '
                                            elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_section_2 + ']'
                                            elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_section_2 + '] '
                                            else:
                                                translated_text += '[' + splitted_text_section_2 + ']'
                    else:
                        translated_text = constructedString
                except:
                    if '[' in constructedString:
                        splitted_text = constructedString.split('[')
                        for splitted_text_section in splitted_text:
                            if ']' in splitted_text_section:
                                splitted_text_2 = splitted_text_section.split(']')
                                for splitted_text_section_2 in splitted_text_2:
                                    if splitted_text_section_2 not in SpecialBuffersReverse:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                            if splitted_text_3 not in SpecialBuffersReverse and splitted_text_4 not in SpecialBuffersReverse:
                                                try:
                                                    translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                                except:
                                                    pass
                                        elif splitted_text_3 in SpecialBuffersReverse:
                                            if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                translated_text += '[' + splitted_text_3 + '] '
                                            elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_3 + ']'
                                            elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_3 + '] '
                                            else:
                                                translated_text += '[' + splitted_text_3 + ']'
                                        elif splitted_text_4 in SpecialBuffersReverse:
                                            if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                translated_text += '[' + splitted_text_4 + '] '
                                            elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_4 + ']'
                                            elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_4 + '] '
                                            else:
                                                translated_text += '[' + splitted_text_3 + ']'
                                    elif splitted_text_section_2 in SpecialBuffersReverse:
                                        if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                            translated_text += '[' + splitted_text_section_2 + '] '
                                        elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                            translated_text += ' [' + splitted_text_section_2 + ']'
                                        elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                            translated_text += ' [' + splitted_text_section_2 + '] '
                                        else:
                                            translated_text += '[' + splitted_text_section_2 + ']'
                    else:
                        translated_text = constructedString
                if constructedString and constructedString[-1] == '$':
                    text = constructedString[:-1]
                    text_newline = text.replace('\n', '\\n')
                    if '[' in text:
                        splitted_text = text_newline.split('[')
                        for splitted_text_section in splitted_text:
                            if ']' in splitted_text_section:
                                splitted_text_2 = splitted_text_section.split(']')
                                for splitted_text_section_2 in splitted_text_2:
                                    if splitted_text_section_2 not in SpecialBuffersReverse:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                            if splitted_text_3 not in SpecialBuffersReverse and splitted_text_4 not in SpecialBuffersReverse:
                                                try:
                                                    translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                                except:
                                                    pass
                                        elif splitted_text_3 in SpecialBuffersReverse:
                                            if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                translated_text += '[' + splitted_text_3 + '] '
                                            elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_3 + ']'
                                            elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_3 + '] '
                                            else:
                                                translated_text += '[' + splitted_text_3 + ']'
                                        elif splitted_text_4 in SpecialBuffersReverse:
                                            if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                translated_text += '[' + splitted_text_4 + '] '
                                            elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_4 + ']'
                                            elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                translated_text += ' [' + splitted_text_4 + '] '
                                            else:
                                                translated_text += '[' + splitted_text_3 + ']'
                                    elif splitted_text_section_2 in SpecialBuffersReverse:
                                        if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                            translated_text += '[' + splitted_text_section_2 + '] '
                                        elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                            translated_text += ' [' + splitted_text_section_2 + ']'
                                        elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                            translated_text += ' [' + splitted_text_section_2 + '] '
                                        else:
                                            translated_text += '[' + splitted_text_section_2 + ']'
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

                            # Split the string into sections of 39 characters without breaking words
                            sections = re.findall(r'(.{1,39}\S(?:\s|$)|\S+)', sanitizedText)

                            # Add '\\n' or '\\p' to the end of each section alternately
                            formatted_sections = []
                            for i, section in enumerate(sections):
                                formatted_sections.append(section + ('\\p' if i % 2 else '\\n') if i < len(sections) - 1 else section)

                            # Join the sections to form the final formatted string
                            formatted_text = ''.join(formatted_sections)

                            # Replace 'xxx' with the original square brackets and their contents
                            for match in matches:
                                formatted_text = formatted_text.replace('xxx', match, 1)

                            # Remove the space before '\\n' or '\\p'
                            formatted_text = formatted_text.replace(' \\n', '\\n').replace(' \\p', '\\p')

                            # print(formatted_text)

                            print(1, string)
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        except:
                            try:
                                print(2, string)
                                f.write('#org @' + string + '\n' + text_newline + '\n\n')
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

                            # Split the string into sections of 39 characters without breaking words
                            sections = re.findall(r'(.{1,39}\S(?:\s|$)|\S+)', sanitizedText)

                            # Add '\\n' or '\\p' to the end of each section alternately
                            formatted_sections = []
                            for i, section in enumerate(sections):
                                formatted_sections.append(section + ('\\p' if i % 2 else '\\n') if i < len(sections) - 1 else section)

                            # Join the sections to form the final formatted string
                            formatted_text = ''.join(formatted_sections)

                            # Replace 'xxx' with the original square brackets and their contents
                            for match in matches:
                                formatted_text = formatted_text.replace('xxx', match, 1)

                            # Remove the space before '\\n' or '\\p'
                            formatted_text = formatted_text.replace(' \\n', '\\n').replace(' \\p', '\\p')

                            # print(formatted_text)

                            print(3, string)
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        except:
                            try:
                                print(4, string)
                                f.write('#org @' + string + '\n' + text_newline + '\n\n')
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
                                    if splitted_text_section_2 not in SpecialBuffersReverse:
                                        if ' ' in splitted_text_section_2:
                                            splitted_text_3 = splitted_text_section_2.split(' ')[0]
                                            splitted_text_4 = splitted_text_section_2.split(' ')[1]
                                            if splitted_text_3 not in SpecialBuffersReverse and splitted_text_4 not in SpecialBuffersReverse:
                                                try:
                                                    translated_text += GoogleTranslator(source='auto', target='es').translate(splitted_text_section_2)
                                                except:
                                                    pass
                                            elif splitted_text_3 in SpecialBuffersReverse:
                                                if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                    translated_text += '[' + splitted_text_3 + '] '
                                                elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                    translated_text += ' [' + splitted_text_3 + ']'
                                                elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                    translated_text += ' [' + splitted_text_3 + '] '
                                                else:
                                                    translated_text += '[' + splitted_text_3 + ']'
                                            elif splitted_text_4 in SpecialBuffersReverse:
                                                if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                                    translated_text += '[' + splitted_text_4 + '] '
                                                elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                                    translated_text += ' [' + splitted_text_4 + ']'
                                                elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                                    translated_text += ' [' + splitted_text_4 + '] '
                                                else:
                                                    translated_text += '[' + splitted_text_3 + ']'
                                    elif splitted_text_section_2 in SpecialBuffersReverse:
                                        if constructedString.split('[')[0] == '' and constructedString.split(']')[1] == ' ':
                                            translated_text += '[' + splitted_text_section_2 + '] '
                                        elif constructedString.split(']')[1] == '' and constructedString.split('[')[0] == ' ':
                                            translated_text += ' [' + splitted_text_section_2 + ']'
                                        elif constructedString.split(']')[1] == ' ' and constructedString.split('[')[0] == ' ':
                                            translated_text += ' [' + splitted_text_section_2 + '] '
                                        else:
                                            translated_text += '[' + splitted_text_section_2 + ']'
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

                            # Identify and replace square brackets and their content with 'xxx'
                            matches = re.findall(r'\[.+?\]', sanitizedText)
                            for match in matches:
                                sanitizedText = sanitizedText.replace(match, 'xxx', 1)

                            # Split the string into sections of 39 characters without breaking words
                            sections = re.findall(r'(.{1,39}\S(?:\s|$)|\S+)', sanitizedText)

                            # Add '\\n' or '\\p' to the end of each section alternately
                            formatted_sections = []
                            for i, section in enumerate(sections):
                                formatted_sections.append(section + ('\\p' if i % 2 else '\\n') if i < len(sections) - 1 else section)

                            # Join the sections to form the final formatted string
                            formatted_text = ''.join(formatted_sections)

                            # Replace 'xxx' with the original square brackets and their contents
                            for match in matches:
                                formatted_text = formatted_text.replace('xxx', match, 1)

                            # Remove the space before '\\n' or '\\p'
                            formatted_text = formatted_text.replace(' \\n', '\\n').replace(' \\p', '\\p')

                            # print(formatted_text)

                            print(5, string)
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        except:
                            try:
                                print(6, string)
                                f.write('#org @' + string + '\n' + text_newline + '\n\n')
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

                            # Identify and replace square brackets and their content with 'xxx'
                            matches = re.findall(r'\[.+?\]', sanitizedText)
                            for match in matches:
                                sanitizedText = sanitizedText.replace(match, 'xxx', 1)

                            # Split the string into sections of 39 characters without breaking words
                            sections = re.findall(r'(.{1,39}\S(?:\s|$)|\S+)', sanitizedText)

                            # Add '\\n' or '\\p' to the end of each section alternately
                            formatted_sections = []
                            for i, section in enumerate(sections):
                                formatted_sections.append(section + ('\\p' if i % 2 else '\\n') if i < len(sections) - 1 else section)

                            # Join the sections to form the final formatted string
                            formatted_text = ''.join(formatted_sections)

                            # Replace 'xxx' with the original square brackets and their contents
                            for match in matches:
                                formatted_text = formatted_text.replace('xxx', match, 1)

                            # Remove the space before '\\n' or '\\p'
                            formatted_text = formatted_text.replace(' \\n', '\\n').replace(' \\p', '\\p')

                            # print(formatted_text)

                            print(7, string)
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        except:
                            try:
                                print(8, string)
                                f.write('#org @' + string + '\n' + text_newline + '\n\n')
                            except:
                                pass
f.close()