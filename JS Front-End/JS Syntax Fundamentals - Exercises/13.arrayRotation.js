function solve(array, rotations) {
  for (let i = 1; i <= rotations; i++) {
    element = array.shift();
    array.push(element);
  }

  console.log(...array);
}
