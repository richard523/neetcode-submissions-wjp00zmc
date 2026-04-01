#line 14
#in python, dictionaries must be immutable and hashable.
#tuple makes the list, 'key' into a 'key' that is immutable and hashable
#therefore key can be used as a dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}

        for s in strs:
            key = [0] * 26 #initializes key for each anagram by incrementing lowercase letters
            for c in s:
                key[ord(c) - ord('a')] += 1 #always grabs lowercase value
            key = tuple(key)
            if key not in anagramGroups:
                anagramGroups[key] = []
            anagramGroups[key].append(s)
        return list(anagramGroups.values())


