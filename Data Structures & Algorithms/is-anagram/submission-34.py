class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letters_map = {}

        for char in s:
            letters_map[char] = letters_map.get(char, 0) + 1

        for char in t:
            if char not in letters_map:
                return False
            letters_map[char] -= 1
            if letters_map[char] < 0:
                return False
        
        return True