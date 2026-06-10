# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # input
            # s
            # t
        # output.
        """
        input: 2 strings:
            s
            t
        output: boolean, true or false
        
        compare two strings.
        
        if length don't match, return false
        
        for i in range(len(s)):
            for j in range(len(t):
            if
                    
        # nlogn sort
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        if sorted_s == sorted_t:
            return True
        else:
            return False
        
        
        # dictionary
        { count : letters } 
            
        """
        
        if len(s) != len(t):
            return False
        
        s_count_hash = {} # how to initialize value to be 0?
        t_count_hash = {}
        
        for char in s:
            if char not in s_count_hash:
                s_count_hash[char] = 0
            s_count_hash[char] += 1
        for char in t:
            if char not in t_count_hash:
                t_count_hash[char] = 0
            t_count_hash[char] += 1
        
        if s_count_hash == t_count_hash:
            return True
        else:
            return False