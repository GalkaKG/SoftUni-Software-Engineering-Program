<?php
// Read the array of integers
$input = trim(fgets(STDIN));

// Split the input string into an array of integers
$numbers = array_map('intval', explode(' ', $input));

// Initialize a variable to store the total sum
$totalSum = 0;

// Iterate through the array, rotating it after each iteration
foreach ($numbers as $number) {
    $totalSum += reverseAndSum($number);
}

// Function to reverse a number and return the sum
function reverseAndSum($number) {
    $reversedNumber = 0;
    while ($number > 0) {
        $digit = $number % 10;
        $reversedNumber = $reversedNumber * 10 + $digit;
        $number = (int)($number / 10);
    }
    return $reversedNumber;
}

// Print the total sum
echo $totalSum . PHP_EOL;
?>
