class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## input
        ### str s
        ### str t

        ## output
        ### bool
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i, e in enumerate(s):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

