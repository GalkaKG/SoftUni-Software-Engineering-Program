function wordsUppercase(input) {

    let expression = input.matchAll(/\w+/gm);
    let result = [];
    for (arr of expression) {
        result.push(arr[0].toUpperCase());
    }

    console.log(result.join(', '));
}

wordsUppercase('Hi, how are you?');

wordsUppercase('hello');
