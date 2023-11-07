const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    return identifyJellyfishAndAddPoints(jellyfish, addPoints);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    let specie = identifySpecies(jellyfish);
    return addPoints(specie);

}

// Score keeping callback function
function addPoints(species) {
    if (species != 'common'){
        return speciesPoints[species];
    }
    return 0;
}

// Helper functions
function identifySpecies(jellyfish) {
    if (jellyfish == 'pink'){
        return 'pink spotted';
    }
    else if (jellyfish == 'blue'){
        return 'blue stinger';
    }
    else if (jellyfish == 'blue'){
        return 'green itches';
    }
    else{
        return 'common';
    }
}

//The Adventure Starts Here! 

for (let i = 0; i < jellyfishDays.length; i++){
    console.log("Let's go jellyfishing!");
    const jellyfishesArr = jellyfishDays[i];
    let score = 0;

    for (let jellyfish = 0; jellyfish < jellyfishDays.length; jellyfish++){
        console.log(`SpongeBob caught a ${jellyfishesArr[jellyfish].color} jellyfish!`);
        score += catchJellyfish(jellyfishesArr[jellyfish].color, identifyJellyfishAndAddPoints);
        console.log(`score: ${score}`);
    }

    console.log('Great job, SpongeBob and Patrick!');
    console.log(`Final score: ${score}`)
}