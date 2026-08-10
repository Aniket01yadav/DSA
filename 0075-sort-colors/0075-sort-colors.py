class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # mx = max(nums)

        # freq = [0]*(mx+1)

        # for i in nums:
        #     freq[i] += 1
        
        # inx = 0
        # for i in range(0, mx+1):
        #     while freq[i] > 0:
        #         nums[inx] = i
        #         freq[i] -= 1
        #         inx  += 1


        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:

            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1