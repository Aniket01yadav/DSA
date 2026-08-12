class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range((len(digits))):
            num = num*10 + digits[i]
        
        num += 1
        list1 = []
        while num > 0:
            temp = num % 10
            list1.append(temp)
            num = num//10
            
        return list1[::-1]