class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if abs(target - total) < abs(target - closest):
                    closest = total
                    
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest
