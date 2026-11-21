class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        count = 1
        end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                count += 1
                end = points[i][1]

        return count