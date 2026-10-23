# Day 16: Freq Map + Ordered Scan


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **First Unique Character in a String** (Primary) | Count character frequencies in a first pass, then re-scan the string in original order to find the first character with a count of 1. | O(n) | O(1) |
| **Sort Characters By Frequency** (Variant) | Build a frequency map and sort characters by descending count, repeating each character by its frequency. | O(n log k) | O(n) |
| **Unique Number of Occurrences** (Variant) | Count occurrences of each number in a dictionary and check whether any frequency value collides in a set. | O(n) | O(n) |
| **Find the Difference** (Variant) | Count characters of the original string and decrement counts while reading the second string to find the extra character. | O(n) | O(1) |
