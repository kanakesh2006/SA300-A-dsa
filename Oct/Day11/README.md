# Day 11: Two Pointers from the End (In-Place Merge)


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Merge Sorted Array** (Primary) | Work backward using three pointers to fill buffer space from the end with the largest available value. | O(m + n) | O(1) |
| **Merge Intervals** (Variant) | Sort by start times and greedily merge contiguous intervals that overlap with the latest added interval. | O(n log n) | O(n) |
| **Merge Two Sorted Lists** (Variant) | Splice nodes together in-place by comparing current values from both lists via a dummy node tracker. | O(n + m) | O(1) |
| **Insert Interval** (Variant) | Append non-overlapping earlier intervals, absorb overlapping intervals into the new interval, and append remainder. | O(n) | O(1) |
| **Merge k Sorted Lists** (Variant) | Merge lists in pairs using divide-and-conquer to combine k lists into a single sorted linked list. | O(N log k) | O(1) |
