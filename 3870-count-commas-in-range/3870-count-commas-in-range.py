class Solution:
    def countCommas(self, n: int) -> int:
        
        diff = n - 1000

        if diff < 0:
            return 0
        else:
            return diff+1