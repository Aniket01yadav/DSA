class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        arr = list(s)
        
        l = 0
        r = len(s)-1

        while l < r:

            while arr[l] not in vowels and l < r:
                l += 1
            while arr[r] not in vowels and l < r:
                r -= 1
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return "".join(arr)
            