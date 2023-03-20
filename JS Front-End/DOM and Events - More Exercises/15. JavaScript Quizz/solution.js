function solve() {
  const sections = Array.from(document.querySelectorAll('section'));
  let result = document.querySelector('.results-inner h1');
  const ulResult = result.parentElement.parentElement;
  let rightAnswers = 0;

  for (const section of sections) {
    section.addEventListener('click', onClick);
  }
 
  function onClick(event) {
    let answear = event.target.textContent;
      if (answear == 'onmouseclick') {
        sections[0].style.display = 'none';
        sections[1].style.display = 'block';
      }

      if (answear == 'onclick') {
        rightAnswers++;
        sections[0].style.display = 'none';
        sections[1].style.display = 'block';  
      }

      if (answear == 'JSON.stringify()') {
        rightAnswers++;
        sections[1].style.display = 'none';
        sections[2].style.display = 'block';  
      }

      if (answear == 'JSON.toString()') {
        sections[1].style.display = 'none';
        sections[2].style.display = 'block';
      }

      if (answear == 'A programming API for HTML and XML documents') {
        rightAnswers++;
        sections[2].style.display = 'none';
        showResult();
      }
   
      if (answear == 'The DOM is your source HTML') {
        sections[2].style.display = 'none';
        showResult();
      }    
  }  
  
  function showResult() {
    if (rightAnswers == 3) {
      result.textContent = "You are recognized as top JavaScript fan!";
      ulResult.style.display = 'block';
  
    } else if (rightAnswers < 3) {
      result.textContent = `You have ${rightAnswers} right answers`;
      ulResult.style.display = 'block';
    }
  }
}
