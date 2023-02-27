function printDNA(num) {
    let sequence = 'ATCGTTAGGG';
    let counter = 0;

    for(i = 0; i < num; i++) {
        let result = '';

        if(counter == 8 || i == 0) {
            counter = 0;
        } else {
            counter += 2;
        }


        if(i == 0 || i % 4 == 0) {
            result = `**${sequence[counter]}${sequence[counter + 1]}**`;  
        } else if(i % 2 == 0) {
            result = `${sequence[counter]}----${sequence[counter + 1]}`;
        } else if(i % 1 == 0 || i % 3 == 0) {
            result = `*${sequence[counter]}--${sequence[counter + 1]}*`;
        }      
        
        console.log(result);
    }

}
