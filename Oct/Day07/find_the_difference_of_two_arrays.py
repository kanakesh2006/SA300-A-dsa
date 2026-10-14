class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set()
        for num in nums1:
            set1.add(num)
            
        set2 = set()
        for num in nums2:
            set2.add(num)
            
        diff1 = []
        for num in set1:
            if num not in set2:
                diff1.append(num)
                
        diff2 = []
        for num in set2:
            if num not in set1:
                diff2.append(num)
                
        return [diff1, diff2]
