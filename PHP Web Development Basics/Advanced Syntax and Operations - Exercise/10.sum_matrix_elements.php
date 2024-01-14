<?php

function sumMatrixElements(array $matrix): array
{
    $rowCount = count($matrix);
    $colCount = count($matrix[0]);
    $sum = 0;

    foreach ($matrix as $row) {
        $sum += array_sum($row);
    }

    return [$rowCount, $colCount, $sum];
}

// Example usage:
$matrixSizes = trim(fgets(STDIN));

// Parse matrix sizes
list($rows, $cols) = array_map('intval', explode(',', $matrixSizes));

// Initialize the matrix
$matrix = [];

// Read matrix elements
for ($i = 0; $i < $rows; $i++) {
    $matrix[$i] = array_map('intval', explode(', ', trim(fgets(STDIN))));
}

// Get the result
$result = sumMatrixElements($matrix);

// Output the result
echo "{$result[0]}\n";
echo "{$result[1]}\n";
echo "{$result[2]}\n";
