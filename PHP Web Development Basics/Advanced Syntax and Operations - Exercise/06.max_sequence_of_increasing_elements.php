<?php
// Read the array of integers
$input = trim(fgets(STDIN));

// Split the input string into an array of integers
$numbers = array_map('intval', explode(' ', $input));

// Initialize variables to keep track of the current and longest increasing subsequences
$currentSequence = [$numbers[0]];
$longestSequence = [];

// Iterate through the array to find the longest increasing subsequence
for ($i = 1; $i < count($numbers); $i++) {
    if ($numbers[$i] > $numbers[$i - 1]) {
        $currentSequence[] = $numbers[$i];
    } else {
        if (count($currentSequence) > count($longestSequence)) {
            $longestSequence = $currentSequence;
        }
        $currentSequence = [$numbers[$i]];
    }
}

// Check if the last subsequence is the longest
if (count($currentSequence) > count($longestSequence)) {
    $longestSequence = $currentSequence;
}

// Print the longest increasing subsequence
echo implode(' ', $longestSequence) . PHP_EOL;
?>
