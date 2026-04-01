class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        #create keys for word s and t
        for i in range(len(s)):
            #increment letters according to s
            count[ord(s[i]) - ord('a')]  += 1
            #subtract letters according to t
            count[ord(t[i]) - ord('a')] -=1
        #this means that if it DOES have the same letters, the key
        #should be all zeroes by cancelling each other out.

        #so if there is a value in count that is not 0, words s and t are not anagrams.
        for val in count:
            if val != 0:
                return False
        return True


        