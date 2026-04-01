class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## input
        ### str s
        ### str t

        ## output
        ### bool
        if len(s) != len(t):
            return False
        y = sorted(s)
        z = sorted(t)
        if y == z:
            return True
        return False