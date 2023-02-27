function phoneBook(array) {

    obj = {}
    for (const data of array) {
        let info = data.split(' ');
        let name = info[0];
        let phone = info[1];
        obj[name] = phone
    }

    for (const property of Object.entries(obj)) {
        console.log(`${property[0]} -> ${property[1]}`);
    }

}
