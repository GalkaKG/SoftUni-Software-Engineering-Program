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
