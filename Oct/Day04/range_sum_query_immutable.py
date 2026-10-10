class NumArray:

    def __init__(self, nums: list[int]):
        self.pref = [0] * len(nums)
        if nums:
            self.pref[0] = nums[0]
            for i in range(1, len(nums)):
                self.pref[i] = self.pref[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pref[right]
        return self.pref[right] - self.pref[left - 1]
