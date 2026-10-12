class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        intervals.append(newInterval)
        intervals.sort()

        ans = []

        for arr in intervals:

            if len(ans) == 0 or ans[-1][1] < arr[0]:
                ans.append(arr)
            else:
                ans[-1][1] = max(ans[-1][1], arr[1])

        return ans 