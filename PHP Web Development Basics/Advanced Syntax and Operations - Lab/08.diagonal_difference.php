<?php
// Read the size of the matrix
$n = intval(trim(fgets(STDIN)));

// Initialize variables to hold the sums of the diagonals
$primaryDiagonalSum = 0;
$secondaryDiagonalSum = 0;

// Read the matrix values and calculate the sums of the diagonals
for ($row = 0; $row < $n; $row++) {
    $rowValues = array_map('intval', explode(' ', trim(fgets(STDIN))));

    // Calculate the sum of the primary diagonal (top-left to bottom-right)
    $primaryDiagonalSum += $rowValues[$row];

    // Calculate the sum of the secondary diagonal (top-right to bottom-left)
    $secondaryDiagonalSum += $rowValues[$n - 1 - $row];
}

// Calculate the absolute difference between the two diagonal sums
$diagonalDifference = abs($primaryDiagonalSum - $secondaryDiagonalSum);

// Output the result
echo $diagonalDifference . PHP_EOL;
?>
