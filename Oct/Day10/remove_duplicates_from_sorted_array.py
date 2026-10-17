class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        slow = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[slow] = nums[read]
                slow += 1
                
        return slow
