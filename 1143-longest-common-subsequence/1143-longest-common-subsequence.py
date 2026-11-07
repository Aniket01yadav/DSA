class Solution:
    def rec(self, i, j, text1, text2, dp):

        if i >= len(text1) or j >= len(text2):
            return 0
        if (i, j) in dp:
            return dp[(i,j)]

        ans = 0
        if text1[i] == text2[j]:
            ans = 1 + self.rec(i+1, j+1, text1, text2, dp)
        else:
            ans = max(self.rec(i+1, j, text1, text2, dp), self.rec(i, j+1, text1, text2, dp))
        dp[(i,j)] = ans
        return dp[(i,j)]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        return self.rec(0, 0, text1, text2, dp)