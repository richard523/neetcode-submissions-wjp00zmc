class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Need to return true if we have exact same characters.

        # of course there's the .reverse() but i'm assuming we want to create
        # a custom implementation of this
        
        # I plan to order both strings. 
        # if ordered strings equal each other, return true
        # else false.

        # And of course if the lengths dont equal each other we can return false immediatey

        if len(s) != len(t):
            return False

        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        if sorted_s == sorted_t:
            return True
        else:
            return False