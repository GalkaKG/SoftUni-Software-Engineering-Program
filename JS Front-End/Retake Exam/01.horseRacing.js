function horseRacing(input) {
    let horses = input.shift().split('|');
    let commands = {
        'Retake': retake,
        'Trouble': trouble,
        'Rage': rage,
        'Miracle': miracle
    }

    for (let i = 0; i < input.length; i++) {
        let command = input[i].split(' ')[0]
        if (command == 'Finish') {
            break;
        }
        commands[command](i);
    }

    function retake(i) {
        let [_, overtakingHorse, overtakenHorse] = input[i].split(' ');
        let idxOfOverTaking = horses.indexOf(overtakingHorse);
        let idxOfOverTaken = horses.indexOf(overtakenHorse);
        let oldPositionOvertaking = idxOfOverTaking;

        if (idxOfOverTaking < idxOfOverTaken) {
            horses.splice(idxOfOverTaken, 1);
            horses.splice(idxOfOverTaken, 0, overtakingHorse);
            
            horses.splice(oldPositionOvertaking, 1);
            horses.splice(oldPositionOvertaking, 0, overtakenHorse);
            console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
        }
    }

    function trouble(i) {
        let [_, horseName] = input[i].split(' ');
        let idxHorseName = horses.indexOf(horseName);
        if (idxHorseName > 0) {
            horses.splice(idxHorseName, 1);
            horses.splice(idxHorseName - 1, 0, horseName);
            console.log(`Trouble for ${horseName} - drops one position.`);
        }
    }

    function rage(i) {
        let [_, horseName] = input[i].split(' ');
        let idxOfHorse = horses.indexOf(horseName);
        
        if (idxOfHorse == horses.length - 2) {
            horses.splice(horses.length + 1, 0, horseName);
            horses.splice(idxOfHorse, 1);
        } else {
            horses.splice(idxOfHorse, 1);
            horses.splice(idxOfHorse + 2, 0, horseName);   
        }
        
   
        console.log(`${horseName} rages 2 positions ahead.`);
    
    }

    function miracle(i) {
        let lastHorse = horses.shift();
        horses.push(lastHorse);
        console.log(`What a miracle - ${lastHorse} becomes first.`);
    }
    
    console.log(horses.join('->'));
    console.log(`The winner is: ${horses[horses.length - 1]}`);
}

// horseRacing((['Bella|Alexia|Sugar',
// 'Retake Alexia Sugar',
// 'Rage Bella',
// 'Trouble Bella',
// 'Finish'])
// )

// horseRacing((['Onyx|Domino|Sugar|Fiona',
// 'Trouble Onyx',
// 'Retake Onyx Sugar',
// 'Rage Domino',
// 'Miracle',
// 'Finish'])
// )

horseRacing((['Fancy|Lilly',
'Retake Lilly Fancy',
'Trouble Lilly',
'Trouble Lilly',
'Finish',
'Rage Lilly'])
);
