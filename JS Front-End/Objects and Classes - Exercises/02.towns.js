function town(input) {

    obj = {};
    for (data of input) {
        info = data.split(' | '); 
        obj.town = info[0];
        obj.latitude = Number(info[1]).toFixed(2);
        obj.longitude = Number(info[2]).toFixed(2);

        console.log(obj)
    }
    
}
