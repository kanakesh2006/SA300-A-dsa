# Day 5: Hashmap Counting & Boyer-Moore


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Majority Element (Hashmap)** (Primary) | Count frequencies manually in a hashmap and return early when count exceeds n // 2. | O(n) | O(n) |
| **Majority Element (Boyer-Moore)** (Primary) | Cancel out opposing elements with a count balance; the true majority candidate remains standing. | O(n) | O(1) |
| **Majority Element II** (Variant) | Extend Boyer-Moore to track two potential candidates, then verify their frequencies in a second pass. | O(n) | O(1) |
| **Degree of an Array** (Variant) | Map each number to its count, first seen index, and last seen index to find the shortest span matching the degree. | O(n) | O(n) |
