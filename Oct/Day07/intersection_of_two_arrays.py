class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        for num in nums1:
            seen.add(num)
            
        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
                
        return res
