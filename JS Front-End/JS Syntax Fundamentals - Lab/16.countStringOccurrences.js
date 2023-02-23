function solve(text, word) {
    let words = text.split(' ');
    let counter = 0;

    for (let current_word of words) {
        if (current_word == word) {
            counter++
        }
    }

    console.log(counter)

}
