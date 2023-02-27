function cat(array) {

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
    }

    for (let catInfo of array) {
        catInfo = catInfo.split(' ')
        let cat = new Cat(catInfo[0], catInfo[1])
        meow(cat)
    }

    function meow(cat) {
        console.log(`${cat.name}, age ${cat.age} says Meow`);
    }

}
