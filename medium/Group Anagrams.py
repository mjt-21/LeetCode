class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHash = {} # Key is sorted anagram, value is list of anagrams
        for s in strs:
            key = str(sorted(s)) # When sorted, all anagrams will become the same!
            if key in anagramHash:
                anagramHash[key].append(s) # If the word finds a key match when sorted, append the anagram to the according list
            else:
                anagramHash[key] = [s] # If no match is found, this is a unique entry; thus make a new value with the sorted word as the key

        return anagramHash.values() # Returning the values returns a list of the lists (groups) of anagrams
