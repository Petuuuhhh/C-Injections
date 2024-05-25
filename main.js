const fs = require('fs');
const dex = require('@pkmn/dex');
const Dex = dex.Dex;
const toID = dex.toID; // Convert to ID readable by Showdown
const Generations = require('@pkmn/data').Generations;
const gens = new Generations(Dex);
const deepmerge = require('deepmerge');
const learnsetsJSON = require('./learnsets.json'); // Showdown learnsets file
const learnsetsGen9 = learnsetsJSON['9'];
const learnsetsGen2 = learnsetsJSON['2'];
const learnsetsMerge = deepmerge(learnsetsGen9, learnsetsGen2);
let learnsets = {};
// Order learnsets alphabetically
for (const mon in learnsetsMerge) {
    if (!learnsetsMerge[mon].learnset) continue;
    learnsets[mon] = {};
    const learnset = learnsetsMerge[mon].learnset;
    const orderedLearnset = Object.keys(learnset).sort().reduce(
      (obj, key) => { 
        obj[key] = learnset[key]; 
        return obj;
      }, 
      {}
    );
    learnsets[mon]['learnset'] = orderedLearnset;
}
const tmhmList = ['focuspunch', 'dragonclaw', 'waterpulse', 'calmmind', 'roar', 'toxic', 'hail', 'bulkup', 'bulletseed', 'hiddenpower', 'sunnyday', 'taunt', 'icebeam', 'blizzard', 'hyperbeam', 'lightscreen', 'protect', 'raindance', 'gigadrain', 'safeguard', 'frustration', 'solarbeam', 'irontail', 'thunderbolt', 'thunder', 'earthquake', 'return', 'dig', 'psychic', 'shadowball', 'brickbreak', 'doubleteam', 'reflect', 'shockwave', 'flamethrower', 'sludgebomb', 'sandstorm', 'fireblast', 'rocktomb', 'aerialace', 'torment', 'facade', 'secretpower', 'rest', 'attract', 'thief', 'steelwing', 'skillswap', 'snatch', 'overheat', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'cut', 'fly', 'surf', 'strength', 'flash', 'rocksmash', 'waterfall', 'dive'];
let sTMHMMoves = 'static const u16 sTMHMMoves[NUM_TMHMS] = {\n';
function PrintsTMHMMoves(learnsetsGen) {
    for (const move of tmhmList) {
        if (move) sTMHMMoves += '\tMOVE_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + ',\n';
    }
    sTMHMMoves += '};';
    fs.writeFileSync('party_menu.h', sTMHMMoves);
}
PrintsTMHMMoves(7);
const NumTMs = 120;
let TMHMLearnsets = '//#define TMHM_LEARNSET(moves) {(u32)(moves), ((u64)(moves) >> 32)}\n//#define TMHM(tmhm) ((u64)1 << (ITEM_##tmhm - ITEM_TM01))\n\n#define TMHM(tmhm)          ((u8) ((ITEM_##tmhm) - ITEM_TM01))\n#define TMHM2(tmhm)          ((u8) ((ITEM_##tmhm) - 318))\n#define TMHM_LEARNSET_END   0xFF\n\n';
async function PrintTMHMLearnsets(speciesGen, learnsetsGen, tmhmList) {
    for (const mon in Dex.data.Species) {
        if (!gens.get(speciesGen).species.get(mon)) continue; // Limit mons to gen's species
        TMHMLearnsets += 'static const u8 s' + gens.get(speciesGen).species.get(mon).name.replace('-', '').replace('.', '').replace(' ', '') + 'TMHMLearnset[] = {\n';
        for (const move of tmhmList) {
            // Limit to a certain gen's learnset compatibility
            const learn = await gens.get(learnsetsGen).learnsets.canLearn(mon, move).then(returnValue => {
                if (returnValue) {
                    if (tmhmList.indexOf(move) + 1 < 10) TMHMLearnsets += '\tTMHM(TM0' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else if (tmhmList.indexOf(move) + 1 <= 64) TMHMLearnsets += '\tTMHM(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else if (tmhmList.indexOf(move) + 1 >= 64 && tmhmList.indexOf(move) + 1 < NumTMs) TMHMLearnsets += '\tTMHM2(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else TMHMLearnsets += '\tTMHM2(HM0' + (tmhmList.indexOf(move) - NumTMs + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                }
            });
            /* if (!learnsets[mon] || !learnsets[mon].learnset) continue;
            if (learnsets[mon].learnset[move]) {
                if (tmhmList.indexOf(move) + 1 < 10) TMHMLearnsets += '\tTMHM(TM0' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else if (tmhmList.indexOf(move) + 1 <= 50) TMHMLearnsets += '\tTMHM(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else if (tmhmList.indexOf(move) + 1 > 50 && tmhmList.indexOf(move) <= 57) TMHMLearnsets += '\tTMHM(HM0' + (tmhmList.indexOf(move) - 49) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else TMHMLearnsets += '\tTMHM2(TM' + (tmhmList.indexOf(move) - 7) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
            } */
        }
        TMHMLearnsets += '\tTMHM_LEARNSET_END,\n};\n\n';
    }
    TMHMLearnsets += 'const u8 *const gTMHMLearnsets[] = {\n';
    for (const mon in Dex.data.Species) {
        if (!gens.get(speciesGen).species.get(mon)) continue;
        TMHMLearnsets += '\t[SPECIES_' + gens.get(speciesGen).species.get(mon).name.toUpperCase().replace('-', '_').replace('.', '_').replace(' ', '_') + '] = s' + gens.get(speciesGen).species.get(mon).name.replace('-', '').replace('.', '').replace(' ', '') + 'TMHMLearnset,\n';
    }
    TMHMLearnsets += '};';
    fs.writeFileSync('tmhm_learnsets.h', TMHMLearnsets);
}
PrintTMHMLearnsets(3, 3, tmhmList);