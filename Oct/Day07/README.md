# Day 7: Hashmap Counting & Multiset


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Intersection of Two Arrays II** (Primary) | Build a frequency map for the smaller array, then decrement counts while scanning the second array to collect matching duplicates. | O(n + m) | O(min(n, m)) |
| **Find Common Characters** (Variant) | Maintain a character frequency map for the first word, updating each character's count to the minimum frequency across all words. | O(n * k) | O(1) |
| **Intersection of Two Arrays** (Variant) | Store elements of the first array in a set and remove matching elements upon first discovery in the second array. | O(n + m) | O(n) |
| **Find the Difference of Two Arrays** (Variant) | Convert both arrays to sets and filter each set for elements not present in the other set. | O(n + m) | O(n + m) |
