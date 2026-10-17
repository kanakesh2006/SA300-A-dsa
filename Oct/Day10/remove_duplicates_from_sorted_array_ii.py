class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
            
        slow = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[slow - 2]:
                nums[slow] = nums[read]
                slow += 1
                
        return slow
