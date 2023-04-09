function sprintReview(input) {
    let n = Number(input.shift())
    let data = {};
    let points = { 
        ToDo: 0,
        'In Progress': 0,
        'Code Review': 0,
        Done: 0
    }

    for (let i = 0; i < n; i++) {
        let [assignee, taskId, title, status, estimatedPoints] = input[i].split(':');
        if (!data.hasOwnProperty(assignee)) {
            data[assignee] = [];
        }
        data[assignee].push({taskId, title, status, estimatedPoints});
        points[status] += Number(estimatedPoints);
    }
    for (let i = 0; i < n; i++) {
        input.shift();
    }

    for (let line of input) {
        let command = line.split(':')[0];
        let assignee = line.split(':')[1];

        if (!data.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
            continue;
        }

        if (command == 'Add New') {
            let [taskId, title, status, estimatedPoints] = line.split(':').slice(2, line.length);
            data[assignee].push({ taskId, title, status, estimatedPoints });
            points[status] += Number(estimatedPoints);

        } else if (command == 'Change Status') {
            let [taskId, newStatus] = line.split(':').slice(2, line.length);
            for (let obj of data[assignee]) {  
                if (obj.taskId == taskId) {
                    points[obj.status] -= obj.estimatedPoints;
                    obj.status = newStatus;
                    points[newStatus] += Number(obj.estimatedPoints);
                } else {
                    console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
                }   
            }

        } else if (command == 'Remove Task') {
            let [assignee, index] = line.split(':').slice(1, line.length);
            if (index < 0 || index >= data[assignee].length) {
                console.log("Index is out of range!");
                continue;
            }
            let pointsForRemove = data[assignee][index].estimatedPoints;
            let currStatus = data[assignee][index].status;
            points[currStatus] -= pointsForRemove;
            delete data[assignee][index];         
        }
    }

    console.log(`ToDo: ${points['ToDo']}pts`)
    console.log(`In Progress: ${points['In Progress']}pts`);
 	  console.log(`Code Review: ${points['Code Review']}pts`);
	  console.log(`Done Points: ${points['Done']}pts`);
    
    if (points['Done'] >= (points['ToDo'] + points['In Progress'] + points['Code Review'])) {
        console.log('Sprint was successful!');
    } else {
        console.log('Sprint was unsuccessful...');
    }
}

sprintReview([
    '5',
    'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
    'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
    'Peter:BOP-1211:POC:Code Review:5',
    'Georgi:BOP-1212:Investigation Task:Done:2',
    'Mariya:BOP-1213:New Account Page:In Progress:13',
    'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
    'Change Status:Peter:BOP-1290:ToDo',
    'Remove Task:Mariya:1',
    'Remove Task:Joro:1',
]);

// sprintReview(  [
//     '4',
//     'Kiril:BOP-1213:Fix Typo:Done:1',
//     'Peter:BOP-1214:New Products Page:In Progress:2',
//     'Mariya:BOP-1215:Setup Routing:ToDo:8',
//     'Georgi:BOP-1216:Add Business Card:Code Review:3',
//     'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
//     'Change Status:Georgi:BOP-1216:Done',
//     'Change Status:Will:BOP-1212:In Progress',
//     'Remove Task:Georgi:3',
//     'Change Status:Mariya:BOP-1215:Done',
// ]
// );
