class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        write_ptr = n - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[write_ptr] = nums[left] * nums[left]
                left += 1
            else:
                res[write_ptr] = nums[right] * nums[right]
                right -= 1
            write_ptr -= 1
            
        return res
