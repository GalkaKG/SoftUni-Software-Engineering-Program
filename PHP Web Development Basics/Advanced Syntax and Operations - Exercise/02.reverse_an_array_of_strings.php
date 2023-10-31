// First solution

<?php
// Read the array of strings
echo "Enter a sequence of space-separated strings: ";
$input = trim(fgets(STDIN));

// Split the input string into an array of strings
$strings = explode(' ', $input);

// Reverse the array manually
$length = count($strings);
for ($i = 0; $i < $length / 2; $i++) {
    $temp = $strings[$i];
    $strings[$i] = $strings[$length - $i - 1];
    $strings[$length - $i - 1] = $temp;
}

// Print the reversed array
echo implode(' ', $strings) . PHP_EOL;
?>


// Second solution

<?php
// Read the array of strings
echo "Enter a sequence of space-separated strings: ";
$input = trim(fgets(STDIN));

// Split the input string into an array of strings
$strings = explode(' ', $input);

// Reverse the array using array_reverse
$reversedStrings = array_reverse($strings);

// Print the reversed array
echo implode(' ', $reversedStrings) . PHP_EOL;
?>
