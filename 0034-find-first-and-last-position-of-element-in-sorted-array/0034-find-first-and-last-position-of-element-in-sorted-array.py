class Solution:
    def lowerBound(self, nums, target):
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
    def upperBound(self, nums, target):
        n = len(nums)
        l = 0 
        r = n-1
        ans = n

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = self.lowerBound(nums, target)
        u = self.upperBound(nums, target)

        if l == u:
            return [-1, -1]
        else:
            return [l, u-1]