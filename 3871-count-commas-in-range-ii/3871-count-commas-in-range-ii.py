class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        min_val = 1000

        while n >= min_val:
            ans += n - min_val + 1
            min_val *= 1000

        return ans