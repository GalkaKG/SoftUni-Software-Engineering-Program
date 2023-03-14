function schoolRegister(input) {
    let studentsData = {};
  
    for (let data of input) {
        let part = data.split(', ')
        let grade = Number(part[1].split(': ')[1])
        let score = Number(part[2].split(': ')[1]);

        if (score >= 3.00) {
            if (!studentsData.hasOwnProperty(grade)) {
                studentsData[grade] = {students: [], score: []};       
            }
            let studentName = part[0].split(': ')[1];
            studentsData[grade].students.push(studentName);
            studentsData[grade].score.push(score)
        }
    }

    const sortedData = Object.entries(studentsData).sort((a, b) => a - b);

    for (let obj of sortedData) {           
        let avgScore = obj[1].score.reduce((a, b) => {
            return a += b
        }, 0)
    
        console.log(`${Number(obj[0]) + 1} Grade`),
        console.log(`List of students: ${obj[1].students.join(', ')}`)
        console.log(`Average annual score from last year: ${(avgScore / obj[1].score.length).toFixed(2)}\n`);
    }
}
