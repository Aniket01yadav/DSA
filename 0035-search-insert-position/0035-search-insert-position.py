class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        ans = n

        while l <= r:

            mid = l + (r-l)//2

            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

        # Another solution
        
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # nums.append(target)
        # nums.sort()

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

                    
