<?php
// Read the input string from the console
$input = trim(fgets(STDIN));

// Split the input string into an array
$data = explode(", ", $input);

// Initialize an associative array to store the total income for each town
$townIncomes = array();

// Loop through the data and calculate the total income for each town
for ($i = 0; $i < count($data); $i += 2) {
    $town = $data[$i];
    $income = intval($data[$i + 1]);

    // If the town key already exists, add the income to it
    if (array_key_exists($town, $townIncomes)) {
        $townIncomes[$town] += $income;
    } else {
        // If the town key doesn't exist, set the income to it
        $townIncomes[$town] = $income;
    }
}

// Loop through the associative array and print the total income for each town
foreach ($townIncomes as $town => $income) {
    echo "$town => $income\n";
}
?>
