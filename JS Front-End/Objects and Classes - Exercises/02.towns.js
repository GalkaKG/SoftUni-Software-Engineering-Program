// 1-st decision:
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


// 2-nd decision:
function town(input) {
    input
       .map((line) => line.split(' | '))
       .map(([town, latitude, longitude]) => ({ town, latitude: Number(latitude).toFixed(2), longitude: Number(longitude).toFixed(2) }))
       .forEach(obj => console.log(obj))
    
}


// Test
town (['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
)
