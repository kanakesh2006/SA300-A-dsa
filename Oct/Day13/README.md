# Day 13: Fixed-Size Sliding Window


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Maximum Average Subarray I** (Primary) | Maintain a running sum for a window of size k by adding the incoming element and subtracting the outgoing element. | O(n) | O(1) |
| **Longest Substring Without Repeating Characters** (Variant) | Expand a variable window while jumping the left pointer past duplicate characters recorded in a hashmap. | O(n) | O(min(m, n)) |
| **Minimum Size Subarray Sum** (Variant) | Expand right pointer until window sum reaches target, then shrink from left to find the minimal window length. | O(n) | O(1) |
| **Find All Anagrams in a String** (Variant) | Slide a fixed window of size len(p) across the string, updating character frequencies in O(1) to find matching anagrams. | O(n) | O(1) |
