function convertToJSON(firstName, lastName, hairColor) {
    obj = {};
    obj.name = firstName;
    obj.lastName = lastName;
    obj.hairColor = hairColor;

    console.log(JSON.stringify(obj));
}
