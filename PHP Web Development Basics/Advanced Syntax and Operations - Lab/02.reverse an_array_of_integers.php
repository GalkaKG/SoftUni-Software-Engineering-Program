<?php
// Read the number of elements (n)
$n = intval(trim(fgets(STDIN)));

// Create an array to store the integers
$integers = [];

// Read the integers and store them in the array
for ($i = 0; $i < $n; $i++) {
    $integers[] = intval(trim(fgets(STDIN)));
}

// Reverse the array
$reversedArray = array_reverse($integers);

// Print the reversed elements separated by spaces
echo implode(' ', $reversedArray) . PHP_EOL;
?>

