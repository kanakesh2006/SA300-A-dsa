class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[slow], nums[read] = nums[read], nums[slow]
                slow += 1
