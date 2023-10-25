<?php
// Read a list of real numbers from the input
$input = array_map('floatval', explode(' ', trim(fgets(STDIN))));

// Initialize an empty dictionary to store counts of each number
$counts = array();

// Sort the input array in ascending order
sort($input);

// Count the occurrences of each number
foreach ($input as $num) {
    $numAsString = strval($num); // Convert the number to a string
    if (array_key_exists($numAsString, $counts)) {
        $counts[$numAsString]++;
    } else {
        $counts[$numAsString] = 1;
    }
}

// Print the numbers in ascending order with their counts
foreach ($counts as $num => $count) {
    echo $num . " -> " . $count . PHP_EOL;
}
?>
