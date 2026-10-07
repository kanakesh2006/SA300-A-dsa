# Day 1: Hashmap Lookup & Two Pointers


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Two Sum** (Primary) | Save numbers in a dictionary as you scan, checking if you've already seen the piece you need to hit the target. | O(n) | O(n) |
| **Two Sum II** (Variant)| Put pointers at the start and end of the sorted list, moving them inward based on if the sum is too big or small. | O(n) | O(1) |
| **3Sum** (Variant) | Sort the list, lock in one number and use two pointers on the remaining list to find triplets that add to zero. | O(n²) | O(1) |
| **3Sum Closest** (Variant) | Same as 3Sum, but just keep track of whatever sum gets the absolute closest to your target value. | O(n²) | O(1) |
| **4Sum** (Variant) | Sort first, lock in two numbers using nested loops and use two pointers to find the remaining pieces. | O(n³) | O(1) |
