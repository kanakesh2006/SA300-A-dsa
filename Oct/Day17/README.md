# Day 17: Longest Common Prefix & String Patterns


| Problem | Approach in Plain English | Time Complexity | Space Complexity |
|---------|---------------------------|-----------------|------------------|
| **Longest Common Prefix** (Primary) | Scan column-by-column across all strings, returning the matched slice upon encountering length exhaustion or character mismatch. | O(s) | O(1) |
| **Repeated Substring Pattern** (Variant) | Check substring prefixes of lengths dividing string length to verify if any repeated prefix reconstructs the string. | O(n * sqrt(n)) | O(n) |
| **Rotate String** (Variant) | Check if lengths match and verify whether the goal string is a substring of the doubled string (s + s). | O(n) | O(n) |
