function roadRadar(speed, area) {
    let limit;
    if (area === "motorway") {
        limit = 130;
    } else if (area === "interstate") {
        limit = 90;
    } else if (area === "city") {
        limit = 50;
    } else {
        limit = 20;
    }

    if (speed <= limit) {
        console.log(`Driving ${speed} km/h in a ${limit} zone`);
    } else {
        let diff = speed - limit;
        let status = "";
        if (diff <= 20) {
            status = "speeding";
        } else if (diff <= 40) {
            status = "excessive speeding";
        } else {
            status = "reckless driving";
        }
        console.log(`The speed is ${diff} km/h faster than the allowed speed of ${limit} - ${status}`);
    }
}
