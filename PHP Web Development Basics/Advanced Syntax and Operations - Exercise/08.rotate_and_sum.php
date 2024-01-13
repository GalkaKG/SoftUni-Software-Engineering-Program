<?php

function rotateAndSum(array $numbers, int $k): array
{
    $n = count($numbers);
    $sum = array_fill(0, $n, 0);

    for ($r = 1; $r <= $k; $r++) {
        $rotated = rotateArray($numbers, $r);
        for ($i = 0; $i < $n; $i++) {
            $sum[$i] += $rotated[$i];
        }
    }

    return $sum;
}

function rotateArray(array $arr, int $r): array
{
    $n = count($arr);
    $rotated = [];

    for ($i = 0; $i < $n; $i++) {
        $rotated[($i + $r) % $n] = $arr[$i];
    }

    return $rotated;
}

// Read input from the console
$input = trim(fgets(STDIN));

$k = (int) trim(fgets(STDIN));

// Convert input string to array of integers
$numbers = array_map('intval', explode(' ', $input));

// Get the rotated and summed array
$result = rotateAndSum($numbers, $k);

// Output the result
echo implode(' ', $result);
