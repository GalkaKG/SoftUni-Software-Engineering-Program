function flightSchedule(matrix) {
    let allFlies = {};
    let printStatus;

    for (let i = 0; i < 3; i++) {
        for (const el of matrix[i]) {
            if (i === 0) {
                let elements = el.split(' ');
                let sector = elements[0];
                let destination = elements.join(' ').replace(sector, '').trim();
                allFlies[sector] = {};
                allFlies[sector].Destination = destination;
                allFlies[sector].Status = 'Ready to fly';
            }
            if (i === 1) {
                let [sector, status] = el.split(' ');
                if (sector in allFlies) {
                    allFlies[sector].Status = status;
                }
            }
            if (i === 2) {
                printStatus = el;
            }
        };
    }

    for (const fly in allFlies) {
        let status = Object.values(allFlies[fly])[1]
        if (status === printStatus) {
            console.log(allFlies[fly]);
        }
    }    
}



// Tests:

flightSchedule([['WN269 Delaware',
'FL2269 Oregon',
 'WN498 Las Vegas',
 'WN3145 Ohio',
 'WN612 Alabama',
 'WN4010 New York',
 'WN1173 California',
 'DL2120 Texas',
 'KL5744 Illinois',
 'WN678 Pennsylvania'],
 ['DL2120 Cancelled',
 'WN612 Cancelled',
 'WN1173 Cancelled',
 'SK430 Cancelled'],
 ['Cancelled']
]);

// flightSchedule([['WN269 Delaware',
// 'FL2269 Oregon',
//  'WN498 Las Vegas',
//  'WN3145 Ohio',
//  'WN612 Alabama',
//  'WN4010 New York',
//  'WN1173 California',
//  'DL2120 Texas',
//  'KL5744 Illinois',
//  'WN678 Pennsylvania'],
//  ['DL2120 Cancelled',
//  'WN612 Cancelled',
//  'WN1173 Cancelled',
//  'SK330 Cancelled'],
//  ['Ready to fly']
// ]);
