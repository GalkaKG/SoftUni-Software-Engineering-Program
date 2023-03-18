function generateReport() {
    let checkBoxes = Array.from(document.querySelectorAll("thead th"));
    let columns = Array.from(document.querySelectorAll("tbody tr"));
    let textArea = document.querySelector("#output");
    let checkBoxArr = [];
    let objArr = [];
  
    for (let i = 0; i < checkBoxes.length; i++) {
      let checkBox = checkBoxes[i].firstElementChild;
      if (checkBox.checked) {
        checkBoxArr.push([i, checkBox.name]);
      }
    }
  
    for (let column of columns) {
      let personObj = {};
      let tds = column.children;
      for (let checkBox of checkBoxArr) {
        personObj[checkBox[1]] = tds[checkBox[0]].textContent;
      }
      objArr.push(personObj);
    }
  
    objArr = JSON.stringify(objArr);
    textArea.value = objArr;
  }
