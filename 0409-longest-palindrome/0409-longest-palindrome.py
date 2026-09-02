class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                ans += 2
            else:
                seen.add(char)

        if seen:
            return ans + 1
        else:
            return ans