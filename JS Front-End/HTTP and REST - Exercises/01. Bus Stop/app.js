function getInfo() {

    const stopId = document.getElementById("stopId").value;
    const url = `http://localhost:3030/jsonstore/bus/businfo/${stopId}`;
   
    const stopName = document.getElementById("stopName");
    const buses = document.getElementById("buses");

    stopName.textContent = 'Loading...'
    buses.replaceChildren();


    fetch(url)
        .then(data => data.json())
        .then(data => {
            stopName.textContent = '';
            buses.textContent = '';
            stopName.textContent = data.name;
            Object.entries(data.buses).forEach(b => {
                const li = document.createElement('li');
                li.textContent = `Bus ${b[0]} arrives in ${b[1]} minutes`
                buses.appendChild(li);
            })

        })   

        .catch(err => {stopName.textContent = 'Error'})

}
