# Day 2: Set Membership & Array Tricks


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Contains Duplicate** (Primary) | Add numbers to a set as you loop, short-circuiting and returning true as soon as you find one already in the set. | O(n) | O(n) |
| **Contains Duplicate II** (Variant) | Maintain a set sliding window of size k, checking for duplicates before dropping elements outside the window. | O(n) | O(k) |
| **Contains Duplicate III** (Variant) | Map numbers to buckets of size (valueDiff + 1) in a sliding window to check for nearby values in O(1) time. | O(n) | O(min(n, k)) |
| **Find All Duplicates in an Array** (Variant) | Use numbers as indices and flip the values at those indices negative to mark elements seen without extra space. | O(n) | O(1) |
| **First Repeating Element** (Variant) | Iterate backwards through the array while maintaining a set to catch the leftmost repeating element's index. | O(n) | O(n) |
