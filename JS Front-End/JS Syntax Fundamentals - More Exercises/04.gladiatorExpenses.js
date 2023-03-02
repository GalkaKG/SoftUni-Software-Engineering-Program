function gladiatorExpenses(lostFightCount, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let sum = 0;
    let counter = 0;

    for (let i = 1; i <= lostFightCount; i++) {
        if (i % 2 == 0) {
            sum += helmetPrice;
        }

        if (i % 3 == 0) {
            sum += swordPrice;
        }

        if (i % 2 == 0 && i % 3 == 0) {
            sum += shieldPrice;
            counter++
        }

        if (counter == 2) {
            sum += armorPrice;
            counter = 0;
        }    
    }

    console.log(`Gladiator expenses: ${sum.toFixed(2)} aureus`);
    
}
