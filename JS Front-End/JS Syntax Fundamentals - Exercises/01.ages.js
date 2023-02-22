function ages(age) {

    if (age < 0) {
        console.log('out of bounds');
    } else if (age <= 2) {
        console.log('baby');
    } else if (age <= 13) {
        console.log('child');
    } else if (age <= 19){
        console.log('teenager');
    } else if (age <= 65) {
        console.log('adult');
    } else if (age >= 66) {
        console.log('elder');
    }

}
