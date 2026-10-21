# Day 12: Squares of a Sorted Array


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Squares of a Sorted Array** (Primary) | Compare absolute values from outer ends and place the larger square into the back of a preallocated array. | O(n) | O(1) extra |
| **Shortest Unsorted Continuous Subarray** (Variant) | Scan left and right to find the outermost indices that violate sorted order relative to running min/max. | O(n) | O(1) |
| **Maximum Absolute Sum of Any Subarray** (Variant) | Track cumulative prefix sums to find the maximum possible spread between the highest and lowest prefix sum. | O(n) | O(1) |
