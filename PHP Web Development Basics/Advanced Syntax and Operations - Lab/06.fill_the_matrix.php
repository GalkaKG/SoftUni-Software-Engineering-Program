<?php
function fillMatrixA($n) {
    $matrix = array();
    $counter = 1;
    $step = $counter;

    for ($row = 0; $row < $n; $row++) {
        for ($col = 0; $col < $n; $col++) {
            $matrix[$row][$col] = $counter;
            $counter += $n;
        }
        $counter = $step + 1;
        $step += 1;
    }

    return $matrix;
}

function fillMatrixB($n) {
    $matrix = array();
    $counter = 1;

    for ($col = 0; $col < $n; $col++) {
        if ($col % 2 == 0) {
            for ($row = 0; $row < $n; $row++) {
                $matrix[$row][$col] = $counter;
                $counter++;
            }
        } else {
            for ($row = $n - 1; $row >= 0; $row--) {
                $matrix[$row][$col] = $counter;
                $counter++;
            }
        }
    }

    return $matrix;
}

function printMatrix($matrix, $n) {
    for ($row = 0; $row < $n; $row++) {
        for ($col = 0; $col < $n; $col++) {
            echo $matrix[$row][$col] . " ";
        }
        echo PHP_EOL;
    }
}

// Input
$input = explode(", ", trim(fgets(STDIN)));
$n = intval($input[0]);
$pattern = $input[1];

if ($pattern == 'A') {
    $matrixA = fillMatrixA($n);
    printMatrix($matrixA, $n);
} elseif ($pattern == 'B') {
    $matrixB = fillMatrixB($n);
    printMatrix($matrixB, $n);
}
?>
