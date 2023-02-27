function storeProvision(stockArr, orderArr) {
    let obj = {};

    for (let i = 0; i < stockArr.length; i += 2) {
        if (i % 2 == 0) {
            obj[stockArr[i]] = Number(stockArr[i + 1])
        }
    }

    for (let i = 0; i < orderArr.length; i += 2) {
        let product = orderArr[i];
        let quantity = Number(orderArr[i + 1]);

        if (product in obj) {
            obj[product] += quantity;
        } else {
            obj[product] = quantity;
        }
    }

    for (data of Object.entries(obj)) {
        console.log(`${data[0]} -> ${data[1]}`)
    }

}
