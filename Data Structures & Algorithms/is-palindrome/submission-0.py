class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Valid Palindrome
        """
        racecar true
        racecat false
        race a car false
        a true
        ' ' true
        
        single char is also palindrome
        
        for char in s:
        
        two pointer problem, 
        . . . . ->
        . . . . <-
        
        
        """
        left = 0
        right = len(s) - 1 # -1 because of index starts at 0, have to offset
        while left < right:
            while left < right and not s[left].isalnum(): # n number of checks per character
                left += 1
            while left < right and not s[right].isalnum(): # n number of checks per character
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True
            