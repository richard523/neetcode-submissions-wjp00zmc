class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## input
        ### str s
        ### str t

        ## output
        ### bool
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False