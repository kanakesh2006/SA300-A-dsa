# Day 4: Prefix Sum Intro


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Running Sum of 1d Array** (Primary) | Modify array in-place by adding each previous element's accumulated value to the current element. | O(n) | O(1) |
| **Range Sum Query - Immutable** (Variant) | Precompute a prefix sum array in constructor so any range sum can be calculated in O(1) using pref[right] - pref[left-1]. | O(1) query | O(n) |
| **Left and Right Sum Differences** (Variant) | Maintain a running left sum while deriving the right sum from total sum to compute absolute differences. | O(n) | O(1) |
| **Richest Customer Wealth** (Variant) | Accumulate wealth for each customer row manually and track the maximum wealth encountered. | O(m * n) | O(1) |
| **Shuffle the Array** (Variant) | Interleave elements from the first half and second half of the array using offset n. | O(n) | O(1) |
