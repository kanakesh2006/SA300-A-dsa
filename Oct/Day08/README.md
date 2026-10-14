# Day 8: Two Pointers from Ends


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Valid Palindrome** (Primary) | Walk two pointers inward from both ends, skipping non-alphanumeric characters and comparing case-insensitively inline. | O(n) | O(1) |
| **Valid Palindrome II** (Variant) | Move pointers inward until a mismatch occurs, then verify if skipping either the left or right character yields a palindrome. | O(n) | O(1) |
| **Palindromic Substrings** (Variant) | Treat each character and adjacent pair as a center, expanding outward to count all palindromic substrings. | O(n²) | O(1) |
| **Palindrome Linked List** (Variant) | Use slow and fast pointers to find the middle node, reverse the second half, and compare values node by node. | O(n) | O(1) |
