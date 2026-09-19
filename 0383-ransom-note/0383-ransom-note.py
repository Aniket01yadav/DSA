class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = defaultdict(int)
        for letter in magazine:
            counts[letter] += 1
        
        for letter in ransomNote:
            if counts[letter] > 0:
                counts[letter] -= 1
            else:
                return False

        return True