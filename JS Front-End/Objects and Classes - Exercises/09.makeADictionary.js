function makeADictionary(data) {
    let filtered = {}
    
    for (let info of data) {
        info = JSON.parse(info)
        filtered[Object.keys(info)] = Object.values(info);    
    }

    let filteredKeys = Object.keys(filtered).sort();

    for (let info of filteredKeys) {
        console.log(`Term: ${info} => Definition: ${filtered[info]}`)
    }

}
