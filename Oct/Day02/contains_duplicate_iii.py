class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        w = valueDiff + 1
        
        for i, num in enumerate(nums):
            b = num // w
            
            if b in buckets:
                return True
            if (b - 1) in buckets and abs(num - buckets[b - 1]) <= valueDiff:
                return True
            if (b + 1) in buckets and abs(num - buckets[b + 1]) <= valueDiff:
                return True
                
            buckets[b] = num
            
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]
                
        return False
