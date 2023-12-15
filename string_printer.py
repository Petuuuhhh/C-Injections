import TextScripts
from TextScripts import TextScripts, pokefirered_sym, JapaneseTextScripts
for symbol in pokefirered_sym:
    string = symbol[3]
    offset = symbol[0][2:]
    offset_actual = symbol[0]
    if string in TextScripts or string in JapaneseTextScripts:
        print(string + ' ' + offset)