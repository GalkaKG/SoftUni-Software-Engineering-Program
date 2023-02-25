function charactersInRange(a, b) {
    let arr = [];
    let start = a.charCodeAt();
    let end = b.charCodeAt();

    if (start > end) {
        start = b.charCodeAt();
        end = a.charCodeAt();
    }
     for (let i = start + 1; i < end; i++) {
        arr.push(String.fromCharCode(i));
     }

     console.log(arr.join(' '));
}
