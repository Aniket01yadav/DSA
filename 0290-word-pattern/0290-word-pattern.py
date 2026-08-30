class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        p = list(p)
        s = s.split(' ')

        if len(p) != len(s):
            return False

        h = {}

        for i in range(len(p)):
            if p[i] in h and s[i] != h[p[i]]:
                return False

            elif p[i] not in h and s[i] in h.values():
                return False

            else:
                h[p[i]] = s[i]

        return True