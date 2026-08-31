class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            sq_sum = 0
            while n > 0:
                digit = n % 10
                sq_sum += digit ** 2
                n //= 10
            n = sq_sum
            
        return n == 1
        