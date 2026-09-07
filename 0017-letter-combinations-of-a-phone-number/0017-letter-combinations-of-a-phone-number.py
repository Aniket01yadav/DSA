class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = [""]

        for i in digits:
            temp = []
            for j in result:
                for k in digit_to_letters[i]:
                    temp.append((j + k))
            result = temp

        return result