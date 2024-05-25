with open('offsets.ini') as input_data:
    # Skips text before the beginning of the interesting block:
    # Reads text until the end of the block:
    for line in input_data:  # This keeps reading the file
        if 'TMHMLearnset' in line:
            mon = line.partition(':')[0]
            offset = line.partition(':')[2].replace(' ', '').replace('\n', '')[2:]
            print("[[NamedAnchors]]\nName = '''data.pokemon.moves." + mon + "''''\nAddress = 0x" + offset + "\nFormat = '''[move.data.pokemon.moves.tms]!FF'''\n")