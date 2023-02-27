function employees(data) {

    obj = {}
    for (info of data) {
        obj.name = info;
        obj.num = info.length;
        console.log(`Name: ${obj.name} -- Personal Number: ${obj.num}`);
    }

}
