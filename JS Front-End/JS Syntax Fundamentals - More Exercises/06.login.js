function login(array) {
    let username = array.shift();
    let counter = 0;

    for (word of array) {
        counter++;

        if (username.split('').reverse().join('') === word) {
            console.log(`User ${username} logged in.`);
        } else {
            if (counter === 4) {
                console.log(`User ${username} blocked!`)
                break;
            }
            console.log("Incorrect password. Try again.");
        } 
   
    }

}

login(['Acer','login','go','let me in','recA']);

login(['momo','omom']);

login(['sunny','rainy','cloudy','sunny','not sunny']);
