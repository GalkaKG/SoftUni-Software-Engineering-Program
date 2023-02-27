function adressBook(array) {
    obj = {};

    for(const info of array) {
        [name, address] = info.split(':');
        obj[name] = address;
    }

    let sortedKeys = Object.keys(obj).sort();

    for (const key of sortedKeys) {
        console.log(`${key} -> ${obj[key]}`);
    }
}
