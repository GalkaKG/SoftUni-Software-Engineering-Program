<?php
// Read the array of integers from the input
$numbers = array_map('intval', explode(' ', trim(fgets(STDIN))));

// Initialize a variable to check if any triples were found
$triplesFound = false;

// Loop through the array to find triples
for ($a = 0; $a < count($numbers); $a++) {
    for ($b = $a + 1; $b < count($numbers); $b++) {
        $sum = $numbers[$a] + $numbers[$b];
        if (in_array($sum, $numbers) && $a != $b) {
            echo "{$numbers[$a]} + {$numbers[$b]} == $sum" . PHP_EOL;
            $triplesFound = true;
        }
    }
}

// Check if no triples were found
if (!$triplesFound) {
    echo "No" . PHP_EOL;
}
?>
