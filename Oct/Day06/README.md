# Day 6: In-place Marking (O(1) Space Trick)


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Find All Numbers Disappeared in an Array** (Primary) | Negate values at index abs(x) - 1 to flag presence, then collect indices that remain positive. | O(n) | O(1) |
| **First Missing Positive** (Variant) | Place each number x at index x - 1 using cyclic swaps, then find the first index where value != index + 1. | O(n) | O(1) |
| **Find All Duplicates in an Array** (Variant) | Negate values at index abs(x) - 1; encountering a value that is already negative reveals a duplicate. | O(n) | O(1) |
