<?php
// Read the first array of integers from the input
$arr1 = array_map('intval', explode(' ', trim(fgets(STDIN))));

// Read the second array of integers from the input
$arr2 = array_map('intval', explode(' ', trim(fgets(STDIN))));

// Determine the lengths of the two arrays
$len1 = count($arr1);
$len2 = count($arr2);

// Determine the maximum length between the two arrays
$maxLen = max($len1, $len2);

// Initialize the result array
$result = [];

// Sum the arrays element by element, duplicating the smaller array as needed
for ($i = 0; $i < $maxLen; $i++) {
    $sum = $arr1[$i % $len1] + $arr2[$i % $len2];
    $result[] = $sum;
}

// Output the result array
echo implode(' ', $result) . PHP_EOL;
?>
