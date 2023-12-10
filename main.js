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
const tmhmList = ['workup', 'dragonclaw', 'psyshock', 'calmmind', 'roar', 'toxic', 'hail', 'bulkup', 'venoshock', 'hiddenpower', 'sunnyday', 'taunt', 'icebeam', 'blizzard', 'hyperbeam', 'lightscreen', 'protect', 'raindance', 'roost', 'safeguard', 'frustration', 'solarbeam', 'smackdown', 'thunderbolt', 'thunder', 'earthquake', 'return', 'leechlife', 'psychic', 'shadowball', 'brickbreak', 'doubleteam', 'reflect', 'sludgewave', 'flamethrower', 'sludgebomb', 'sandstorm', 'fireblast', 'rocktomb', 'aerialace', 'torment', 'facade', 'flamecharge', 'rest', 'attract', 'thief', 'lowsweep', 'round', 'echoedvoice', 'overheat', 'steelwing', 'focusblast', 'energyball', 'falseswipe', 'scald', 'fling', 'chargebeam', 'skydrop', 'brutalswing', 'quash', 'willowisp', 'acrobatics', 'embargo', 'explosion', 'shadowclaw', 'payback', 'smartstrike', 'gigaimpact', 'rockpolish', 'auroraveil', 'stoneedge', 'voltswitch', 'thunderwave', 'gyroball', 'swordsdance', 'fly', 'psychup', 'bulldoze', 'frostbreath', 'rockslide', 'xscissor', 'dragontail', 'infestation', 'poisonjab', 'dreameater', 'grassknot', 'swagger', 'sleeptalk', 'uturn', 'substitute', 'flashcannon', 'trickroom', 'wildcharge', 'surf', 'snarl', 'naturepower', 'darkpulse', 'waterfall', 'dazzlinggleam', 'confide', 'cut', 'fly', 'surf', 'strength', 'flash', 'rocksmash', 'waterfall', 'dive'];
const NumTMs = 100;
let TMHMLearnsets = '';
async function PrintTMHMCompatibility(speciesGen, learnsetsGen, tmhmList) {
    for (const mon in Dex.data.Species) {
        if (!gens.get(speciesGen).species.get(mon)) continue; // Limit mons to gen's species
        TMHMLearnsets += 'static const u8 s' + gens.get(speciesGen).species.get(mon).name.replace('-', '').replace('.', '').replace(' ', '') + 'TMHMLearnset[] = {\n';
        for (const move of tmhmList) {
            // Limit to a certain gen's learnset compatibility
            /* const learn = await gens.get(learnsetsGen).learnsets.canLearn(mon, move).then(returnValue => {
                if (returnValue) {
                    if (tmhmList.indexOf(move) + 1 < 10) TMHMLearnsets += '\tTMHM(TM0' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else if (tmhmList.indexOf(move) + 1 < NumTMs) TMHMLearnsets += '\tTMHM(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else TMHMLearnsets += '\tTMHM(HM' + (tmhmList.indexOf(move) - 99) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                }
            }); */
            if (!learnsets[mon] || !learnsets[mon].learnset) continue;
            if (learnsets[mon].learnset[move]) {
                if (tmhmList.indexOf(move) + 1 < 10) TMHMLearnsets += '\tTMHM(TM0' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else if (tmhmList.indexOf(move) + 1 < NumTMs) TMHMLearnsets += '\tTMHM(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else TMHMLearnsets += '\tTMHM(HM' + (tmhmList.indexOf(move) - 99) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
            }
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
PrintTMHMCompatibility(3, 7, tmhmList);