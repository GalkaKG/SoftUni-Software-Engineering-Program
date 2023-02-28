function wordTracker (data) {
    let result = new Map();

    let words = data.shift().split(' ');
    for (let word of words) {
        result.set(word, 0);
    }
    for (let word of data) {
        if(result.has(word)) {
            let oldValue = result.get(word);
            result.set(word, oldValue + 1);
        }
    }

    let sortResult = Array.from(result).sort(([keyA, valueA], [keyB, valueB]) => {
        return valueB - valueA
    });

    for(let [key, value] of sortResult) {
        console.log(key, '-', value)
    }

}
