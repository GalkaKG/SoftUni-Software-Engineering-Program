function loadingBar(number) {
    let bar = '[..........]'

    if (number == 100) {
        console.log('100% Complete!')
    } else {
        for (let i = 0; i < number; i+=10) {
            bar = bar.replace('.', '%')
        }
        console.log(`${number}% ${bar}`);
        console.log('Still loading...');  
    }
}
