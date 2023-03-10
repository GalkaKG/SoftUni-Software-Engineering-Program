function solve() {
    const infoElement = document.querySelector('div#info span.info');
    const departBtn = document.getElementById('depart');
    const arriveBtn = document.getElementById('arrive');
    
    let nextStopId = 'depot';
    let stopName = '';

    async function depart() {
        try {
            const res = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${nextStopId}`);
            if (!res.ok) {
                let error = new Error();
                error.status = res.status;
                error.statusText = res.statusText;
                throw error;
            }
            const data = await res.json();
            stopName = data.name;
            nextStopId = data.next;
            infoElement.textContent = `Next stop ${stopName}`;
            departBtn.disabled = true;
            arriveBtn.disabled = false;

        }
        catch (error) {
            infoElement.textContent = 'Error';
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        }

    }

    async function arrive() {
        infoElement.textContent = `Arriving at ${stopName}`;
        departBtn.disabled = false;
        arriveBtn.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
