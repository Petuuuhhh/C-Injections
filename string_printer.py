import TextScripts
from TextScripts import TextScripts, pokefirered_sym
for symbol in pokefirered_sym:
    string = symbol[3]
    offset = symbol[0][2:]
    offset_actual = symbol[0]
    if string in TextScripts:
        print(string + ' 08' + offset)