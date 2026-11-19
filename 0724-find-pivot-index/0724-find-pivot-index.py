class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        sum1 = sum(nums)
        for i in range(len(nums)):
            right = sum1 - nums[i] - left
            if left == right:
                return i
            left += nums[i]
        return -1