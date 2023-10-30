<?php
// Read the input from the console
echo "Enter chemical elements (comma-separated): ";
$input = trim(fgets(STDIN)); // Using fgets to read input

// Split the input string into an array using commas as the delimiter
$elements = explode(', ', $input);

// Count the frequency of each element
$elementCount = array_count_values($elements);

// Find and print the elements that appear exactly once
$uniqueElements = array_filter($elementCount, function ($count) {
    return $count === 1;
});

if (!empty($uniqueElements)) {
    $uniqueElementsString = implode(' ', array_keys($uniqueElements));
    echo $uniqueElementsString . PHP_EOL;
} else {
    echo "No unique elements found." . PHP_EOL;
}
?>
