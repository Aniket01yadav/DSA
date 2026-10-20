class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        a = x
        while x > 0:
            temp = x % 10
            rev = rev*10 + temp
            x = x//10
        return rev == a