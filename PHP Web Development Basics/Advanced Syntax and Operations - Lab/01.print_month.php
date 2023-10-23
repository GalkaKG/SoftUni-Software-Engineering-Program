<?php
// Array of month names
$monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

// Prompt the user for input
echo "";
$monthNumber = intval(trim(fgets(STDIN))); // Read user input and convert to an integer

// Check if the input is in the valid range
if ($monthNumber >= 1 && $monthNumber <= 12) {
    $monthName = $monthNames[$monthNumber - 1]; // Subtract 1 to get the correct array index
    echo $monthName . PHP_EOL;
} else {
    echo "Invalid Month!" . PHP_EOL;
}
?>
