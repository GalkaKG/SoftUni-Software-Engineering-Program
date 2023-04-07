function movingTarget(input) {
    let targets = input.shift().split(' ').map((num) => Number(num));

    let line = input.shift();
    while (line !== 'End') {
        let [command, index, other] = line.split(' ');
        index = Number(index);
        other = Number(other);

        if (command == 'Shoot') {
            shoot(index, other);
        } else if (command == 'Add') {
            add(index, other);
        } else if (command == 'Strike') {
            strike(index, other);
        }

        line = input.shift();
    }

    console.log(targets.join('|'));

    function shoot(idx, power) {
        if (validateIdx(idx)) {
            targets[idx] -= power;
        }
        if (targets[idx] <= 0) {
            targets.splice(idx, 1);
        }
        return targets;
    }

    function add(idx, value) {
        if (validateIdx(idx)) {
            return targets.splice(idx, 0, value);
        } 
        console.log('Invalid placement!');
    }
 
    function strike(idx, radius) {
        if (validateIdx(idx) && validateIdx(idx - radius) && validateIdx(idx + radius)) {
            return targets.splice(idx - radius, radius + radius + 1);     
        } 
        console.log('Strike missed!');
    }

    function validateIdx(idx) {
        return idx >= 0 && idx < targets.length;
    }
}

movingTarget((["52 74 23 44 96 110",
"Shoot 5 10",
"Shoot 1 80",
"Strike 2 1",
"Add 22 3",
"End"])
);

// movingTarget((["1 2 3 4 5",
// "Strike 0 1",
// "End"])
// )
