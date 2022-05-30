function shopping (input) {
    let budget = Number(input[0]);
    let countVGA = Number(input[1]);
    let countCPU = Number(input[2]);
    let countRAM = Number(input[3]);
    let priceCPU= (countVGA * 250) * 0.35;
    let priceRAM = (countVGA * 250) * 0.10;
    let sumForAll = countVGA * 250 + countCPU * priceCPU + countRAM * priceRAM;

    if (countVGA > countCPU) {
        sumForAll= sumForAll - (sumForAll * 0.15);
    }
    let left = Math.abs(sumForAll - budget);
    if (budget >= sumForAll) {
        console.log(`You have ${left.toFixed(2)} leva left!`);
    } else {
        console.log(`Not enough money! You need ${left.toFixed(2)} leva more!`)
    }
}
