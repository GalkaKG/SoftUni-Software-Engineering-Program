function memoryGame(input) {
    let line = input.shift().split(' ');
    let moves = 0;

    while(line.length > 0) {
        let indexes = input.shift();
        if (indexes === 'end') {
            break;
        }
        moves++;
        let [idx1, idx2] = indexes.split(' ');
        idx1 = Number(idx1);
        idx2 = Number(idx2);
        if (idx1 === idx2 || idx1 < 0 || idx1 >= line.length || idx2 < 0 || idx2 >= line.length) {
            let start = line.length / 2;
            let forAdd = [`-${moves}a`, `-${moves}a`]
            line.splice(start, 0, ...forAdd)
            console.log("Invalid input! Adding additional elements to the board");
        } else if (line[idx1] === line[idx2]) {
            console.log(`Congrats! You have found matching elements - ${line[idx1]}!`); 
            if (idx1 > idx2) {
                line.splice(idx1, 1);
                line.splice(idx2, 1);
            } else {
                line.splice(idx1, 1);
                line.splice(idx2 - 1, 1);
            }
        } else if(line[idx1] !== line[idx2]) {
            console.log("Try again!");
        }
    }

    if (line.length > 0) {
        console.log(`Sorry you lose :(\n${line.join(' ')}`);
    } else {
        console.log(`You have won in ${moves} turns!`);
    }
}


// Tests
memoryGame( [
    "1 1 2 2 3 3 4 4 5 5", 
    "1 0",
    "-1 0",
    "1 0", 
    "1 0", 
    "1 0", 
    "end"
    ]
    )

memoryGame([
    "a 2 4 a 2 4", 
    "0 3", 
    "0 2",
    "0 1",
    "0 1", 
    "end"
    ]
    )

// memoryGame([
//     "a 2 4 a 2 4", 
//     "4 0", 
//     "0 2",
//     "0 1",
//     "0 1", 
//     "end"
//     ]
//     )
