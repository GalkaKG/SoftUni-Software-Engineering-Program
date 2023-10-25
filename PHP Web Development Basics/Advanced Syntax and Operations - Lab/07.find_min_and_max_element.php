<?php
function findMinAndMax($matrix) {
    $min = $matrix[0][0];
    $max = $matrix[0][0];

    foreach ($matrix as $row) {
        foreach ($row as $element) {
            if ($element < $min) {
                $min = $element;
            }
            if ($element > $max) {
                $max = $element;
            }
        }
    }

    return array('min' => $min, 'max' => $max);
}

// Input
$input = explode(", ", trim(fgets(STDIN)));
$n = intval($input[0]);
$m = intval($input[1]);

$matrix = array();

for ($i = 0; $i < $n; $i++) {
    $matrix[$i] = array_map('intval', explode(", ", trim(fgets(STDIN))));
}

// Find the minimum and maximum elements
$minMax = findMinAndMax($matrix);

// Output
echo "Min: " . $minMax['min'] . PHP_EOL;
echo "Max: " . $minMax['max'] . PHP_EOL;
?>
