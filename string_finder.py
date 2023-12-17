import TextScripts
from TextScripts import TextScripts, pokefirered_sym, charMap, CharMap, SpecialBuffersReverse, SpecialBuffers
from Japanese import JapaneseChars, Japanese
import re
from deep_translator import GoogleTranslator
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
# from tqdm import tqdm

def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)

nineWidths = ['B_BUFF2', 'B_OPPONENT_MON1_NAME', 'B_COPY_VAR_1', 'B_COPY_VAR_2', 'B_COPY_VAR_3']
SOURCE_ROM = "BPRE0.gba"
num3 = 0
target_language = 'es'

f = open("output.txt", "w", encoding="utf-8")
with open(SOURCE_ROM, 'rb+') as rom:
    for symbol_index in range(len(pokefirered_sym)):
        symbol = pokefirered_sym[symbol_index]
        string = symbol[3]
        offset = symbol[0][2:]
        offset_actual = symbol[0]
        rom_offset = offset_actual
        # if string == 'PokemonMansion_Text_PressSecretSwitchJP':
        if int('0x' + offset_actual, 16) >= int('0x08000000', 16):
            if string in TextScripts:
                constructed_string = ''
                constructed_string2 = ''
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
                                constructed_string += CharMap[ordROM]
                            num = num + 1
                            offset_actual = hex(int(offset_actual, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + offset_actual), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            if num2 > -1:
                                if ordROM_2 in SpecialBuffers:
                                    # print(2, SpecialBuffers[ordROM_2])
                                    constructed_string += '[' + SpecialBuffers[ordROM_2] + ']'
                                    offset_actual = hex(int(offset_actual, 16) + int('02', 16)).replace('0x', '')
                                elif ordROM_3 in SpecialBuffers:
                                    # print(3, SpecialBuffers[ordROM_3])
                                    constructed_string += '[' + SpecialBuffers[ordROM_3] + ']'
                                    offset_actual = hex(int(offset_actual, 16) + int('03', 16)).replace('0x', '')
                                elif ordROM_5 in SpecialBuffers:
                                    # print(5, SpecialBuffers[ordROM_5])
                                    constructed_string += '[' + SpecialBuffers[ordROM_5] + ']'
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
                                constructed_string2 += Japanese[returnValue]
                            num = num + 1
                            rom_offset = hex(int(rom_offset, 16) + int('01', 16)).replace('0x', '')
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                        else:
                            num = 0
                            if num2 > -1:
                                if ordROM_2 in SpecialBuffers:
                                    # print(2, SpecialBuffers[ordROM_2])
                                    constructed_string2 += '[' + SpecialBuffers[ordROM_2] + ']'
                                    rom_offset = hex(int(rom_offset, 16) + int('02', 16)).replace('0x', '')
                                elif ordROM_3 in SpecialBuffers:
                                    # print(3, SpecialBuffers[ordROM_3])
                                    constructed_string2 += '[' + SpecialBuffers[ordROM_3] + ']'
                                    rom_offset = hex(int(rom_offset, 16) + int('03', 16)).replace('0x', '')
                                elif ordROM_5 in SpecialBuffers:
                                    # print(5, SpecialBuffers[ordROM_5])
                                    constructed_string2 += '[' + SpecialBuffers[ordROM_5] + ']'
                                    rom_offset = hex(int(rom_offset, 16) + int('05', 16)).replace('0x', '')
                                else:
                                    rom_offset = hex(int(rom_offset, 16) + int('01', 16)).replace('0x', '')
                            num2 = num2 + 1
                            rom.seek(int(('0x' + rom_offset), 16) - 0x08000000)
                            ordROM = ord(rom.read(1))
                except:
                    pass
                english = ''
                japanese = ''
                if '[' in constructed_string2:
                    splitted_text = constructed_string2.split('[')
                    for splitted_text_section in splitted_text:
                        if ']' in splitted_text_section:
                            splitted_text_2 = splitted_text_section.split(']')
                            for splitted_text_section_2 in splitted_text_2:
                                if splitted_text_section_2 in SpecialBuffersReverse:
                                    if constructed_string2.split('[')[0] == '' and constructed_string2.split(']')[1] == ' ':
                                        japanese += '[' + splitted_text_section_2 + '] '
                                    elif constructed_string2.split(']')[1] == '' and constructed_string2.split('[')[0] == ' ':
                                        japanese += ' [' + splitted_text_section_2 + ']'
                                    elif constructed_string2.split(']')[1] == ' ' and constructed_string2.split('[')[0] == ' ':
                                        japanese += ' [' + splitted_text_section_2 + '] '
                                    else:
                                        japanese += '[' + splitted_text_section_2 + ']'
                                else:
                                    try:
                                        japanese += GoogleTranslator(source='auto', target=target_language).translate(splitted_text_section_2)
                                    except:
                                        pass
                        else:
                            try:
                                japanese += GoogleTranslator(source='auto', target=target_language).translate(splitted_text_section)
                            except:
                                pass
                else:
                    japanese = GoogleTranslator(source='auto', target=target_language).translate(constructed_string2)
                if '[' in constructed_string:
                    splitted_text = constructed_string.split('[')
                    for splitted_text_section in splitted_text:
                        if ']' in splitted_text_section:
                            splitted_text_2 = splitted_text_section.split(']')
                            for splitted_text_section_2 in splitted_text_2:
                                if splitted_text_section_2 in SpecialBuffersReverse:
                                    if constructed_string.split('[')[0] == '' and constructed_string.split(']')[1] == ' ':
                                        english += '[' + splitted_text_section_2 + '] '
                                    elif constructed_string.split(']')[1] == '' and constructed_string.split('[')[0] == ' ':
                                        english += ' [' + splitted_text_section_2 + ']'
                                    elif constructed_string.split(']')[1] == ' ' and constructed_string.split('[')[0] == ' ':
                                        english += ' [' + splitted_text_section_2 + '] '
                                    else:
                                        english += '[' + splitted_text_section_2 + ']'
                                else:
                                    try:
                                        english += GoogleTranslator(source='auto', target=target_language).translate(splitted_text_section_2)
                                    except:
                                        pass
                        else:
                            try:
                                english += GoogleTranslator(source='auto', target=target_language).translate(splitted_text_section)
                            except:
                                pass
                else:
                    english = GoogleTranslator(source='auto', target=target_language).translate(constructed_string)
                if english:
                    text_newline = english.replace('\n', '\\n')
                    line_endings = 'npl'
                    line_endings_store = ''
                    pos = 0
                    try:
                        for char in english:
                            if char == '\\':
                                try:
                                    if english[pos + 1] in line_endings:
                                        line_endings_store = line_endings_store + english[pos + 1]
                                except:
                                    pass
                            pos = pos + 1
                        sanitizedText = english.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')

                        # Identify and replace square brackets and their content with 'xxx'
                        matches = re.findall(r'\[.+?\]', sanitizedText)
                        for match in matches:
                            sanitizedText = sanitizedText.replace(match, 'xxx', 1)

                        # Check if sanitizedText is less than 37 characters
                        if len(sanitizedText) <= 37:
                            formatted_text = sanitizedText
                        else:
                            # Split the string into sections of 37 characters without breaking words
                            sections = re.findall(r'(.{1,37}\S(?:\s|$)|\S+)', sanitizedText)

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

                        lang2 = nlp(formatted_text)._.language['language']
                        if lang2 == target_language:
                            print(1, string)
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        else:
                            lang = 'ja'
                    except:
                        try:
                            if lang2 == target_language:
                                print(2, string)
                                f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                            else:
                                lang = 'ja'
                        except:
                            pass
                else:
                    line_endings = 'npl'
                    line_endings_store = ''
                    pos = 0
                    try:
                        for char in english:
                            if char == '\\':
                                try:
                                    if english[pos + 1] in line_endings:
                                        line_endings_store = line_endings_store + english[pos + 1]
                                except:
                                    pass
                            pos = pos + 1
                        sanitizedText = english.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')

                        # Identify and replace square brackets and their content with 'xxx'
                        matches = re.findall(r'\[.+?\]', sanitizedText)
                        for match in matches:
                            sanitizedText = sanitizedText.replace(match, 'xxx', 1)

                        # Check if sanitizedText is less than 37 characters
                        if len(sanitizedText) <= 37:
                            formatted_text = sanitizedText
                        else:
                            # Split the string into sections of 37 characters without breaking words
                            sections = re.findall(r'(.{1,37}\S(?:\s|$)|\S+)', sanitizedText)

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

                        lang2 = nlp(formatted_text)._.language['language']
                        if lang2 == target_language:
                            print(3, string)
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        else:
                            lang = 'ja'
                    except:
                        try:
                            if lang2 == target_language:
                                print(4, string)
                                f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                            else:
                                lang = 'ja'
                        except:
                            pass
                if lang == 'ja':
                    text_newline = japanese.replace('\n', '\\n')
                    line_endings = 'npl'
                    line_endings_store = ''
                    pos = 0
                    try:
                        for char in japanese:
                            if char == '\\':
                                try:
                                    if japanese[pos + 1] in line_endings:
                                        line_endings_store = line_endings_store + japanese[pos + 1]
                                except:
                                    pass
                            pos = pos + 1
                        sanitizedText = japanese.replace('\\n', ' ').replace('\\p', ' ').replace('\\l', ' ')

                        # Identify and replace square brackets and their content with 'xxx'
                        matches = re.findall(r'\[.+?\]', sanitizedText)
                        for match in matches:
                            sanitizedText = sanitizedText.replace(match, 'xxx', 1)

                        # Check if sanitizedText is less than 37 characters
                        if len(sanitizedText) <= 37:
                            formatted_text = sanitizedText
                        else:
                            # Split the string into sections of 37 characters without breaking words
                            sections = re.findall(r'(.{1,37}\S(?:\s|$)|\S+)', sanitizedText)

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
                            f.write('#org @' + string + '\n' + formatted_text + '\n\n')
                        except:
                            pass
f.close()