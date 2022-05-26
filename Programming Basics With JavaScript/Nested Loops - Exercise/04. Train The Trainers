function trainTheTrainers (input) {
    let index = 0;
    let people = Number(input[index]);
    index++;
    let command = input[index];
    index++;

    let counter = 0;
    let sumGrade = 0;

    while (command !== "Finish") {
        let name = command;
        counter++;
        let sumTempGrade = 0;
        for (let i = 0; i < people; i++) {
            let grade = Number(input[index]);
            index++;
            sumTempGrade += grade;
        }
        let tempAvgGrade = sumTempGrade / people;
        console.log(`${name} - ${tempAvgGrade.toFixed(2)}.`);
        sumGrade += tempAvgGrade;

        command = input[index];
        index++;

    }

    let avg = sumGrade / counter;
    console.log(`Student's final assessment is ${avg.toFixed(2)}.`);
}
