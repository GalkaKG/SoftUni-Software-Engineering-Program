// 1-st decision:
function employees(data) {

    obj = {}
    for (info of data) {
        obj.name = info;
        obj.num = info.length;
        console.log(`Name: ${obj.name} -- Personal Number: ${obj.num}`);
    }
}



// 2-nd decision:
function employees(input) {
    Object.entries(
        input.reduce((data, employee) => {
            data[employee] = employee.length;
            return data; 
        }, {})
    ).forEach(([employee, length]) => {
        console.log(`Name: ${employee} -- Personal Number: ${length}`);
    })  
}



// Test:
employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]
    )
