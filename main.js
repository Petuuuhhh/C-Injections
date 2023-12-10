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
const gen3ou = require('./gen3ou.json').pokemon; // [Gen 3] OU Smogon usage statistics
const tmhmList = ['workup', 'dragonclaw', 'psyshock', 'calmmind', 'roar', 'toxic', 'hail', 'bulkup', 'venoshock', 'hiddenpower', 'sunnyday', 'taunt', 'icebeam', 'blizzard', 'hyperbeam', 'lightscreen', 'protect', 'raindance', 'roost', 'safeguard', 'frustration', 'solarbeam', 'smackdown', 'thunderbolt', 'thunder', 'earthquake', 'return', 'leechlife', 'psychic', 'shadowball', 'brickbreak', 'doubleteam', 'reflect', 'sludgewave', 'flamethrower', 'sludgebomb', 'sandstorm', 'fireblast', 'rocktomb', 'aerialace', 'torment', 'facade', 'flamecharge', 'rest', 'attract', 'thief', 'lowsweep', 'round', 'echoedvoice', 'overheat', 'steelwing', 'focusblast', 'energyball', 'falseswipe', 'scald', 'fling', 'chargebeam', 'skydrop', 'brutalswing', 'quash', 'willowisp', 'acrobatics', 'embargo', 'explosion', 'shadowclaw', 'payback', 'smartstrike', 'gigaimpact', 'rockpolish', 'auroraveil', 'stoneedge', 'voltswitch', 'thunderwave', 'gyroball', 'swordsdance', 'fly', 'psychup', 'bulldoze', 'frostbreath', 'rockslide', 'xscissor', 'dragontail', 'infestation', 'poisonjab', 'dreameater', 'grassknot', 'swagger', 'sleeptalk', 'uturn', 'substitute', 'flashcannon', 'trickroom', 'wildcharge', 'surf', 'snarl', 'naturepower', 'darkpulse', 'waterfall', 'dazzlinggleam', 'confide', 'cut', 'fly', 'surf', 'strength', 'flash', 'rocksmash', 'waterfall', 'dive'];
let sTMHMMoves = 'static const u16 sTMHMMoves[NUM_TMHMS] = {\n';
function PrintsTMHMMoves(learnsetsGen) {
    for (const move of tmhmList) {
        sTMHMMoves += '\tMOVE_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + ',\n';
    }
    sTMHMMoves += '};';
    fs.writeFileSync('party_menu.h', sTMHMMoves);
}
PrintsTMHMMoves(7);
const NumTMs = 100;
let gMoveLearnerMoves = '#define MOVE_LEARNER_MOVES_SPECIES_OFFSET 20000\n#define MOVE_LEARNER_MOVES_TERMINATOR 0xFFFF\n#define move_learner_moves(species, moves...) (SPECIES_##species + MOVE_LEARNER_MOVES_SPECIES_OFFSET), moves\n\n';
async function PrintgMoveLearnerMoves(speciesGen, learnsetsGen, list) {
    for (const mon in Dex.data.Species) {
        if (!gens.get(speciesGen).species.get(mon)) continue; // Limit mons to gen's species
        // for (const move of list) {
            // Limit to a certain gen's learnset compatibility
            /* const learn = await gens.get(learnsetsGen).learnsets.canLearn(mon, move).then(returnValue => {
                if (returnValue) {
                    if (tmhmList.indexOf(move) + 1 < 10) TMHMLearnsets += '\tTMHM(TM0' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else if (tmhmList.indexOf(move) + 1 < NumTMs) TMHMLearnsets += '\tTMHM(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                    else TMHMLearnsets += '\tTMHM(HM' + (tmhmList.indexOf(move) - 99) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                }
            }); */
            // Include every move a mon can learn
            /* if (!learnsets[mon] || !learnsets[mon].learnset) continue;
            if (learnsets[mon].learnset[move]) {
                if (tmhmList.indexOf(move) + 1 < 10) TMHMLearnsets += '\tTMHM(TM0' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else if (tmhmList.indexOf(move) + 1 <= NumTMs) TMHMLearnsets += '\tTMHM(TM' + (tmhmList.indexOf(move) + 1) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
                else TMHMLearnsets += '\tTMHM(HM0' + (tmhmList.indexOf(move) - 99) + '_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + '),\n';
            } */
        // }
        if (!gen3ou[gens.get(speciesGen).species.get(mon).name]) continue;
        gMoveLearnerMoves += '\tmove_learner_moves(' + gens.get(speciesGen).species.get(mon).name.toUpperCase().replace('-', '_').replace('.', '_').replace(' ', '_') + ',';
        let HiddenPower = 0;
        for (let move in gen3ou[gens.get(speciesGen).species.get(mon).name].moves) {
            if (move == 'Nothing') continue;
            if (move.includes('Hidden Power')) {
                move = 'hiddenpower';
                HiddenPower += 1;
            }
            if (toID(move) != 'hiddenpower') gMoveLearnerMoves += '\n\t\t\t  MOVE_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + ',';
            else if (HiddenPower < 2) gMoveLearnerMoves += '\n\t\t\t  MOVE_' + gens.get(learnsetsGen).moves.get(move).name.toUpperCase().replace('-', '_').replace(/ /g, '_') + ',';
        }
        gMoveLearnerMoves += '),\n\n';
    }
    gMoveLearnerMoves += '\tMOVE_LEARNER_MOVES_TERMINATOR\n};';
    fs.writeFileSync('move_learner_moves.h', gMoveLearnerMoves);
}
PrintgMoveLearnerMoves(3, 7);