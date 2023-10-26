<?php
// Read the sequence of words from the input
$words = explode(' ', trim(fgets(STDIN)));

// Initialize an associative array to count occurrences of words
$wordCount = array();

// Initialize an array to store the result elements
$result = array();

// Count the occurrences of words
foreach ($words as $word) {
    // Convert the word to lowercase for case-insensitive comparison
    $word = strtolower($word);

    if (array_key_exists($word, $wordCount)) {
        $wordCount[$word]++;
    } else {
        $wordCount[$word] = 1;
    }
}

// Iterate through the word counts and append words with odd counts to the result
foreach ($wordCount as $word => $count) {
    if ($count % 2 == 1) {
        $result[] = $word;
    }
}

// Output the result elements in lowercase
echo implode(', ', $result) . PHP_EOL;
?>
