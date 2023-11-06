<?php
// Read the value of n
echo "Enter n: ";
$n = intval(trim(fgets(STDIN)));

// Read the value of k
echo "Enter k: ";
$k = intval(trim(fgets(STDIN)));

// Initialize an array to store the sequence
$sequence = array(1);

// Generate the sequence
for ($i = 1; $i < $n; $i++) {
    // Calculate the sum of the previous k elements (if fewer than k elements are available, sum all of them)
    $sum = 0;
    for ($j = max(0, $i - $k); $j < $i; $j++) {
        $sum += $sequence[$j];
    }
    
    $sequence[] = $sum;
}

// Print the generated sequence
echo implode(' ', $sequence) . PHP_EOL;
?>
