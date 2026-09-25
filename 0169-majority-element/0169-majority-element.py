class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        dict1 = {}
        n = len(nums)
        for i in range(n):

            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1

        for key, value in dict1.items():
            if value >= n / 2:
                return key