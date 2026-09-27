class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stact = []
        
        for ch in s:
            temp = ""
            if ch != ')':
                stact.append(ch)
            else:
                while stact[-1] != "(":
                    temp += stact.pop()
                stact.pop()                    
                
                for i in temp:
                    stact.append(i)
                 
        return "".join(stact)