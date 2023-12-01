class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # If lengths are different, they definitely can't be anagrams

        for c in set(s): # set() to only loop through unique values, no duplicates
            if s.count(c) != t.count(c): # If counts are different for a character, they can't be anagrams
                return False
                
        return True # All counts were the same, thus anagrams
