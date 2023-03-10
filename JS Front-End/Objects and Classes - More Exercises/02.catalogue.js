function catalogue(input) {
    let objects = {};

    for (const line of input) {
        let key = line[0];
        if (objects.hasOwnProperty(key)) {
            objects[key].push(line)
        } else {
            objects[key] = [line]; 
        }
    }

    let ordered = Object.keys(objects).sort().reduce(
      (obj, k) =>  {
        obj[k] = objects[k];
        return obj;
      }, {}
    );

    for (objKey in ordered) {  
        console.log(objKey); 
        ordered[objKey].sort((a,b) => a.localeCompare(b));
      
        ordered[objKey].forEach(element => {
            element = element.split(' : ');
            console.log(`  ${element[0]}: ${element[1]}`);
        });
    }   
}
