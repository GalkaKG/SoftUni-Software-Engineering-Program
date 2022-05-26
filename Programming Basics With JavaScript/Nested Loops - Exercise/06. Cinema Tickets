function cinemaTickets (input) {
    let index = 0;
   
    let command = input[index];
    index++;

    let studentTicketCount = 0;
    let standartTicketCount = 0;
    let kidTicketCount = 0;
    let ticketCounter = 0;
     
    while (command !== "Finish") {
        let name = command;
        let freeSpace = Number(input[index]);
        index++;

        let type = input[index];
        index++;
        let tempTicketCounter = 0;

        while (type !== "End") {
            switch (type) {
                case "student": studentTicketCount++; break;
                case "standard": standartTicketCount++; break;
                case "kid": kidTicketCount++; break;
            }
            tempTicketCounter++;

            if (tempTicketCounter >= freeSpace) {
                break;
            }
            type = input[index];
            index++;
        }

        let capacity = tempTicketCounter / freeSpace * 100;
        ticketCounter += tempTicketCounter;

        console.log(`${name} - ${capacity.toFixed(2)}% full.`);
        command = input[index];
        index++;
    }

    let studentP = studentTicketCount / ticketCounter * 100;
    let standartP = standartTicketCount / ticketCounter * 100;
    let kidP = kidTicketCount / ticketCounter * 100;

    console.log(`Total tickets: ${ticketCounter}`);
    console.log(`${studentP.toFixed(2)}% student tickets.`);
    console.log(`${standartP.toFixed(2)}% standard tickets.`);
    console.log(`${kidP.toFixed(2)}% kids tickets.`)
}
