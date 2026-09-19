class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        dict2 = {}

        for i in ransomNote:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in magazine:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
            
        for key in dict1:
            if key not in dict2 or dict2[key] < dict1[key]:
                return False

        return True