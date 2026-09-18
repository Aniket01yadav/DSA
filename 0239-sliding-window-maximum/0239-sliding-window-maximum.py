class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = []
        head = 0  
        res = []

        for i in range(len(nums)):
        
            while len(q) > head and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if q[head] <= i - k:
                head += 1

            if i >= k - 1:
                res.append(nums[q[head]])

        return res