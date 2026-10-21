# Day 14: Sliding Window + Hashmap


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Contains Duplicate II** (Primary) | Store the latest index of each number in a dictionary and check if the distance to a previous occurrence is within k. | O(n) | O(min(n, k)) |
| **Longest Repeating Character Replacement** (Variant) | Maintain rolling character counts in a variable window, shrinking whenever non-majority characters exceed k replacements. | O(n) | O(1) |
| **Permutation in String** (Variant) | Roll a fixed window of size len(s1) across s2, adjusting character counts in O(1) to detect matching permutations. | O(n) | O(1) |
