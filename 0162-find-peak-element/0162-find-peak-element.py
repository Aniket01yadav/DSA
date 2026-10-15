class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        maxi = nums[0]
        j = 0
        for i in range(len(nums)):
            if maxi < nums[i]:
                maxi = nums[i]
                j = i

        return j

        
