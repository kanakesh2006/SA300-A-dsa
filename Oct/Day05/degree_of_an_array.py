class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first = {}
        last = {}
        count = {}
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
            
        degree = max(count.values())
        min_len = len(nums)
        
        for num in count:
            if count[num] == degree:
                sub_len = last[num] - first[num] + 1
                if sub_len < min_len:
                    min_len = sub_len
                    
        return min_len
