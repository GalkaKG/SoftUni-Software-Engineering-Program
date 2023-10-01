function addClass() {
    let showClass = document.getElementsByClassName("show");
    let asideElement = document.getElementsByTagName("aside")[0];
    if (showClass.length == 0) {
        asideElement.classList.add("moveDown");
    }
    else {
        asideElement.classList.remove("moveDown");
    }
}