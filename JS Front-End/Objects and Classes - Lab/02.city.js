function city (obj) {
    for (const property in obj) {
        console.log(`${property} -> ${obj[property]}`)
    }
}
