class Solution:
    def firstRepeated(self, arr: list[int]) -> int:
        seen = set()
        min_idx = -1
        
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] in seen:
                min_idx = i + 1
            else:
                seen.add(arr[i])
                
        return min_idx
