function lockedProfile() {
    const main = document.getElementById("main");

    fetch(`http://localhost:3030/jsonstore/advanced/profiles`)
    .then(response => response.json())
    .then(display);

    function display(data){
        main.innerHTML = "";
        let num = 1;
        Object.values(data).forEach(current => {
            createCard(current,num);
            num++;
        });

        const allButtons = Array.from(document.querySelectorAll("button"));
        allButtons.forEach(button => {
            button.addEventListener("click",checkLock);
        })
    }

    function createCard(data,num){
        console.log(data);
        main.innerHTML += `<div class="profile">
				<img src="./iconProfile2.png" class="userIcon" />
				<label>Lock</label>
				<input type="radio" name="user${num}Locked" value="lock" checked>
				<label>Unlock</label>
				<input type="radio" name="user${num}Locked" value="unlock"><br>
				<hr>
				<label>Username</label>
				<input type="text" name="user${num}Username" value="${data.username}" disabled readonly />
				<div class="hiddenInfo" id="user${num}HiddenFields">
					<hr>
					<label>Email:</label>
					<input type="email" name="user${num}Email" value="${data.email}" disabled readonly />
					<label>Age:</label>
					<input type="email" name="user${num}Age" value="${data.age}" disabled readonly />
				</div>
				<button>Show more</button>
			</div>`
    }

    function checkLock(e){
        let button = e.currentTarget;
        let unlock = e.currentTarget.parentElement.querySelector('input[value="unlock"]')
        let hiddenInputs = Array.from(e.currentTarget.parentElement.querySelectorAll(".hiddenInfo > input"));
        let hiddenLabels = Array.from(e.currentTarget.parentElement.querySelectorAll(".hiddenInfo > label"));
        if(unlock.checked && button.textContent === "Show more"){
            hiddenInputs.forEach(element => element.style.display = "block");
            hiddenLabels.forEach(element => element.style.display = "block");
            e.currentTarget.textContent = "Hide it";
        } else if(unlock.checked && button.textContent === "Hide it"){
            e.currentTarget.textContent = "Show more";
            hiddenInputs.forEach(element => element.style.display = "none");
            hiddenLabels.forEach(element => element.style.display = "none");
        }
    }
}
