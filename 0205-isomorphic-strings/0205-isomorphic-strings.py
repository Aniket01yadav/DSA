class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        

        map_s = {}
        map_t = {}
        for i in range(len(s)):
            
            if map_s.get(s[i]) != map_t.get(t[i]):
                return False
            
            map_s[s[i]] = i+1
            map_t[t[i]] = i+1
            
        return True