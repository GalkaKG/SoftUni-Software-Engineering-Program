function bonusScore (input) {
    let scores = Number(input[0]);
    if (scores <= 100) {
        bonus = 5;
    } else if (scores > 1000) {
        bonus = scores * 0.10;
    } else  {
        bonus = scores * 0.20;
    }
    if (scores % 2 == 0) {
        bonus += 1;
    } else if (scores % 10 == 5){
        bonus += 2;
    }
  console.log(bonus);
  console.log(scores + bonus);
}
