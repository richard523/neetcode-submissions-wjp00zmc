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

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
        # account manager aoede
        # aoede 

        # Last year, account manager. 

        # Meet customers quarterly. 

        # Ornob 
        # ornob@amazon.com

        # bhavana@aoede.dev