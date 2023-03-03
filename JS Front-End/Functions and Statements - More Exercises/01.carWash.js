function carWash(array) {
    let carClean = 0;

    for (const element of array) {
        if (element === 'soap') {
            carClean += 10;
        } else if (element === 'water') {
            carClean += carClean * 0.20;
        } else if (element === 'vacuum cleaner') {
            carClean += carClean * 0.25;
        } else if (element === 'mud') {
            carClean -= carClean * 0.10;
        }
    }

    console.log(`The car is ${carClean.toFixed(2)}% clean.`);

}
