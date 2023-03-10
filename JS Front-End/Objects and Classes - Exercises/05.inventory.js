// 1-st decision:
function inventory(array) {
    let heroes = [];

    class Hero {
        constructor(name,level,items){
            this.name = name,
            this.level = level,
            this.items = items
        }
    }

    for(const data of array) {
        let [name, level, items] = data.split(' / ');
        let currentHero = new Hero(name,Number(level),items);
        heroes.push(currentHero);
    }

    heroes.sort((a, b) => {
        return a.level - b.level
    });

    for (let hero of heroes) {
        console.log(`Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items}`)
    }
}


// 2-nd decision:
function inventory(input) {
    let heroes = [];

    for (const line of input) {
        let [ hero, level, items] = line.split(' / ');
        level = Number(level);
        heroes.push({ hero, level, items });
    }

    let sortedHeroes = heroes.sort((heroA, heroB) => heroA.level - heroB.level);
    for (const { hero, level, items } of sortedHeroes) {
        console.log(`Hero: ${hero}`);
        console.log(`level => ${level}`);
        console.log(`items => ${items}`);
    }
}


// Test:
inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ]
    );
