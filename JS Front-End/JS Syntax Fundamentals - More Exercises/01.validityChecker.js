function solve(x1, y1, x2, y2) {

    let coordinates = [[x1,y1], [x2,y2]];
    for(let coords of coordinates) {
        let formula1 = Math.sqrt((0 - coords[0])**2 + (0 - coords[1])**2);

        if(formula1 === Math.floor(formula1)){
            console.log(`{${coords[0]}, ${coords[1]}} to {0, 0} is valid`);
        } else {
            console.log(`{${coords[0]}, ${coords[1]}} to {0, 0} is invalid`);
        }
    }

    let formula2 = Math.sqrt((x2- x1)**2 + (y2 - y1)**2);
    if (formula2 == Math.floor(formula2)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`)
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`)
    }

}
