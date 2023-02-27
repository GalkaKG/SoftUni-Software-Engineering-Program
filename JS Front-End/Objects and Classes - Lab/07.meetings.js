function meetings(array) {
    meetings = {};

    for (const data of array) {
        let info = data.split(' ');

        if(Object.keys(meetings).includes(info[0])) {
            console.log(`Conflict on ${info[0]}!`);
        } else {
            console.log(`Scheduled for ${info[0]}`);
            meetings[info[0]] = info[1];
        }
    }

    for (const property in meetings) {
        console.log(`${property} -> ${meetings[property]}`)
    }

}
