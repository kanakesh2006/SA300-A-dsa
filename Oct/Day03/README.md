# Day 3: XOR & Bit Manipulation


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Single Number** (Primary) | XOR all numbers together; duplicate pairs cancel out to zero, leaving only the unique element. | O(n) | O(1) |
| **Single Number II** (Variant) | Maintain two bitmasks representing numbers seen once and twice to reset bits appearing three times. | O(n) | O(1) |
| **Single Number III** (Variant) | XOR all numbers to get a ^ b, find the rightmost set bit, and partition numbers to find both unique values. | O(n) | O(1) |
| **Missing Number** (Variant) | XOR array elements with their indices 0 to n so matching numbers cancel out, leaving the missing index. | O(n) | O(1) |
| **Find the Difference** (Variant) | XOR ASCII character codes of both strings together; matching characters cancel out to reveal the extra letter. | O(n) | O(1) |
