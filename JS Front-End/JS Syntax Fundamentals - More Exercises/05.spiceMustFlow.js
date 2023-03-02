function spiceMustFlow(startingYield) {
    let days = 0;
    let yield = 0;
    let spiceExtracted = 0;

    while (startingYield >= 100) {
        yield = startingYield - 26;
        startingYield -= 10;  
        spiceExtracted += yield;
        days++;    
    }
    
    spiceExtracted -= 26;
    if(spiceExtracted < 0) {
        spiceExtracted = 0;
    }

    console.log(days);
    console.log(spiceExtracted);

}

spiceMustFlow(111);

spiceMustFlow(450);
