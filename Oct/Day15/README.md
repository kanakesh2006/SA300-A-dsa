# Day 15: Character Frequency Counting


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Valid Anagram** (Primary) | Check length equality first, then count characters in parallel dictionaries and compare key-value pairs. | O(n) | O(1) |
| **Minimum Window Substring** (Variant) | Expand sliding window until all target character frequencies match, then contract from the left to find minimal window. | O(n + m) | O(1) |
| **Group Anagrams** (Variant) | Generate a 26-length character frequency tuple for each word and group words with matching frequency keys in a hashmap. | O(n * k) | O(n * k) |
