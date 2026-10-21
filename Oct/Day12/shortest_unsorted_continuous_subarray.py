class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        start = -1
        end = -2
        
        max_seen = nums[0]
        min_seen = nums[-1]
        
        for i in range(1, n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i
                
        for i in range(n - 2, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                start = i
                
        return end - start + 1 if end >= start else 0
