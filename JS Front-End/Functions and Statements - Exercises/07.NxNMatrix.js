// 1-st decision:

function matrix(n) {
    for(let i = 0; i < n; i++) {
        let output = '';
        for (let j = 0; j < n; j++) {
            output += String(n) + ' ';
        }
        console.log(output)
    }
}



// 2-nd decision:

(n) => new Array(n).fill(new Array(n).fill(n)).forEach(row => console.log(row.join(' ')));




