function bitcoinMining(goldPerDayArr) {

    let bitcoinPrice = 11949.16;
    let goldGrPrice = 67.51;
    let countBitcoins = 0;
    let money = 0;
    let firstBitcoinDay = 0;

    for (let i = 0; i <= goldPerDayArr.length - 1; i++) {
        let gold = goldPerDayArr[i];

        if ((i + 1) % 3 === 0) {
            gold -= (gold * 0.30);
            
        }

        money += gold * goldGrPrice;

        while (money >= bitcoinPrice) {

            if (money >= bitcoinPrice) {
                countBitcoins++;
                money -= bitcoinPrice;

                if (countBitcoins === 1) {
                    firstBitcoinDay = i + 1;
                }
            }
        }
  
    }
    
    console.log(`Bought bitcoins: ${countBitcoins}`);

    if (countBitcoins > 0) {
        console.log(`Day of the first purchased bitcoin: ${firstBitcoinDay}`);
    }
    console.log(`Left money: ${money.toFixed(2)} lv.`);  

}

bitcoinMining([100, 200, 300]);

bitcoinMining([50, 100]);

bitcoinMining([3124.15, 504.212, 2511.124]);
