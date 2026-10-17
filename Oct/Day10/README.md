# Day 10: Read/Write Pointers


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Remove Duplicates from Sorted Array** (Primary) | Advance read pointer and overwrite at slow pointer whenever a new unique element is found. | O(n) | O(1) |
| **Sort Colors** (Variant) | Use three pointers (low, curr, high) to partition 0s, 1s, and 2s into their respective regions in one pass. | O(n) | O(1) |
| **Move Zeroes** (Variant) | Swap non-zero elements encountered by read pointer to the slow write pointer to bubble zeroes to the end. | O(n) | O(1) |
| **Remove Duplicates from Sorted Array II** (Variant) | Allow at most two duplicates by writing only when current number differs from the element at slow - 2. | O(n) | O(1) |
