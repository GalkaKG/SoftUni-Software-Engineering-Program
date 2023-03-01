function pianist(input) {
    let n = input.shift();
    let collection = {};

    for(let i = 0; i < n; i++) {
        let [piece, composer, key] = input.shift().split('|');
        collection[piece] = [composer, key];
    }

    line = input.shift();

    while(line !== 'Stop') {
        let [command, piece, composer, key] = line.split('|');

        if (command == 'Add') {
            if (Object.keys(collection).includes(piece)) {
                console.log(`${piece} is already in the collection!`)
            } else {
                collection[piece] = [composer, key];
                console.log(`${piece} by ${composer} in ${key} added to the collection!`)
            }

        } else if (command == 'Remove') {
            if(Object.keys(collection).includes(piece)) {
                delete collection[piece]
                console.log(`Successfully removed ${piece}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`)
            }

        } else if (command == 'ChangeKey') {
            if(Object.keys(collection).includes(piece)) {
                collection[piece][1] = composer ;
                console.log(`Changed the key of ${piece} to ${composer}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            }

        }

        line = input.shift();
    }

    for (const piece in collection) {
        let details = collection[piece]
        console.log(`${piece} -> Composer: ${details[0]}, Key: ${details[1]}`);
    }

}
