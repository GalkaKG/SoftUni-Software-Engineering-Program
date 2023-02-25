function passValidator(input) {
    let flag1 = true;
    let flag2 = true;
    let flag3 = true;
    let digitCounter = 0;

    if (input.length < 6 || input.length > 10) {
        console.log("Password must be between 6 and 10 characters");
        flag1 = false;
    }

    for (let char of input) {
        if ((char.charCodeAt(0) < 65 || char.charCodeAt(0) > 90) &&
            (char.charCodeAt(0) < 97 || char.charCodeAt(0) > 122) &&
            (char.charCodeAt(0) < 48 || char.charCodeAt(0) > 57)) {
            flag2 = false;
            console.log("Password must consist only of letters and digits");
            break;
        }
    }

    for (let digit of input) {
        flag3 = false;
        if (digit.charCodeAt(0) >= 48 && digit.charCodeAt(0) <= 57) {
            digitCounter++;
        }
        if (digitCounter >= 2) {
            flag3 = true;
            break;
        }
    }

    if (!flag3) {
        console.log("Password must have at least 2 digits");
    }

    if(flag1 && flag2 && flag3){
        console.log("Password is valid");
    }
}
