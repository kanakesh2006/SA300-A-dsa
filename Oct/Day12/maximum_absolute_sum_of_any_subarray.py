class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        curr = 0
        max_pref = 0
        min_pref = 0
        
        for num in nums:
            curr += num
            if curr > max_pref:
                max_pref = curr
            if curr < min_pref:
                min_pref = curr
                
        return max_pref - min_pref
