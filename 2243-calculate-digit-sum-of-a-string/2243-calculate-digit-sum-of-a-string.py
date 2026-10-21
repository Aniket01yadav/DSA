class Solution:
    def digitSum(self, s: str, k: int) -> str:

        if len(s) <= k:
            return s
        ans = "" 
        for i in range(0,len(s),k):
            group = s[i : i + k]
            digit_sum = 0
            for digit in group:
                digit_int = int(digit)
                digit_sum += digit_int
            ans += str(digit_sum)
        
        return self.digitSum(ans, k)