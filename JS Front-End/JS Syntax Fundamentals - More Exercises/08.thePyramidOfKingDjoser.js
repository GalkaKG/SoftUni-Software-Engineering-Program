function thePyramidOfKingDjoser(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;
    let steps = 0;
    
    while (base > 0) {

        steps++;

        if (base === 1 || base === 2) {
            gold += (base * base) * increment;
            break;
        }
        
        if (steps % 5 == 0) {
           lapis += ((base * base) - (base - 2) ** 2) * increment;
           stone += ((base - 2) ** 2) * increment;
         
        } else {
           stone += ((base - 2) ** 2) * increment;
           marble += ((base * base) - ((base - 2) ** 2)) * increment
        }

        base -= 2;
       
    }    

    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);


    let height = Math.floor(steps * increment);
    console.log(`Final pyramid height: ${height}`);

}
