function heroesOfCodeAndLogic(input) {
    let n = Number(input.shift());
    let heroes = {};
    let commands = {
        'CastSpell': castSpell,
        'TakeDamage': takeDamage,
        'Recharge': recharge,
        'Heal': heal
    }

    for (let i = 0; i < n; i++) {
        let [heroName, hp, mp] = input[i].split(' ');
        heroes[heroName] = { hp: Number(hp), mp: Number(mp) };    
    }

    for (let i = n; i < input.length; i++) {
        if (input[i] == 'End') {
            break;
        }
        let command = input[i].split(' - ')[0];
        commands[command](i);
    }

    function castSpell(i) {
        let [_, heroName, mpNeeded, spellName] = input[i].split(' - ');
        mpNeeded = Number(mpNeeded);
        
        if (heroes[heroName].mp < mpNeeded) {
            console.log(`${heroName} does not have enough MP to cast ${spellName}!`);
        } else {
            heroes[heroName].mp -= mpNeeded
            console.log(`${heroName} has successfully cast ${spellName} and now has ${heroes[heroName].mp} MP!`);
        }
    }

    function takeDamage(i) {
        let [_, heroName, damage, attacker] = input[i].split(' - ');
        damage = Number(damage);
        
        heroes[heroName].hp -= damage;
        if (heroes[heroName].hp <= 0) {
            console.log(`${heroName} has been killed by ${attacker}!`);
            delete heroes[heroName]
        } else {
            console.log(`${heroName} was hit for ${damage} HP by ${attacker} and now has ${heroes[heroName].hp} HP left!`);
        }
    }

    function recharge(i) {
        let [_, heroName, amount] = input[i].split(' - ');
        amount = Number(amount);
        let amountRecovered = 0;
        
        if ((heroes[heroName].mp + amount) > 200) {
            amountRecovered = 200 - heroes[heroName].mp;
            heroes[heroName].mp = 200;
        } else {
            amountRecovered = amount;
            heroes[heroName].mp += amount;
        }
        console.log(`${heroName} recharged for ${amountRecovered} MP!`);
    }

    function heal(i) {
        let [_, heroName, amount] = input[i].split(' - ');
        amount = Number(amount);
        let recoveredAmount = 0;
        if ((heroes[heroName].hp + amount) > 100) {
            recoveredAmount = 100 - heroes[heroName].hp;
            heroes[heroName].hp = 100;
        } else {
            recoveredAmount = amount;
            heroes[heroName].hp += amount;
        }
        console.log(`${heroName} healed for ${recoveredAmount} HP!`);
    }

    for (let hero in heroes) {
        console.log(`${hero}\n HP: ${heroes[hero].hp}\n MP: ${heroes[hero].mp}`
        );
    }
}

// heroesOfCodeAndLogic([2,
//     'Solmyr 85 120',
//     'Kyrre 99 50',
//     'Heal - Solmyr - 10',
//     'Recharge - Solmyr - 50',
//     'TakeDamage - Kyrre - 66 - Orc',
//     'CastSpell - Kyrre - 15 - ViewEarth',
//     'End'
//     ]);

heroesOfCodeAndLogic([4,
    'Adela 90 150',
    'SirMullich 70 40',
    'Ivor 1 111',
    'Tyris 94 61',
    'Heal - SirMullich - 50',
    'Recharge - Adela - 100',
    'CastSpell - Tyris - 1000 - Fireball',
    'TakeDamage - Tyris - 99 - Fireball',
    'TakeDamage - Ivor - 3 - Mosquito',
    'End'
    ])
