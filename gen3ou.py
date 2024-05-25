import json
f = open('gen3ou.json')
gen3ou = json.load(f)
moves = {}
for mon in gen3ou['pokemon']:
    for move in gen3ou['pokemon'][mon]['moves']:
        if move not in moves:
            moves[move] = gen3ou['pokemon'][mon]['count'] * gen3ou['pokemon'][mon]['moves'][move]
        else:
            moves[move] += gen3ou['pokemon'][mon]['count'] * gen3ou['pokemon'][mon]['moves'][move]
moves = dict(sorted(moves.items(), key=lambda item: item[1], reverse=True))
for move in moves:
    print(move, moves[move])
f.close()