function orders (product, quantity) {
    let price;

    switch (product) {
        case 'coffee': 
            price = 1.50;
            break;
        case 'water':
            price = 1.00;
            break;
        case 'coke':
            price = 1.40;
            break;
        case 'snacks':
            price = 2.00;
            break;
    }

    price *= quantity;

    console.log(`${price.toFixed(2)}`);

}
