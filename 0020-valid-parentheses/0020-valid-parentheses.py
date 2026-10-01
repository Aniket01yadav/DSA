class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 == 1:
            return False

        stack = []

        for ch in s:

            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)

            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()

                if ch == ")" and top != "(":
                    return False
                elif ch == '}' and top != "{":
                    return False
                elif ch == ']' and top != "[":
                    return False

        return len(stack) == 0