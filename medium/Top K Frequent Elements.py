class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsHash = {} # Key is number, value is count
        for n in nums:
            numsHash[n] = numsHash.get(n, 0) + 1 # Increments count if already in dict, sets to 1 if not

        freq = [[] for i in range(len(nums) + 1)] # Index is count, list at that index is of all nums with such count!

        for n, c in numsHash.items(): # .items() returns tuple of dict keys & values; more easily iterable for us
            freq[c].append(n) # Populate freq list with counts from dict

        result = [] # To hold the top K frequent nums
        for i in range(len(freq) - 1, 0, -1): # Simply loop from the greatest to least index, aka greatest to least count nums
            for n in freq[i]:
                result.append(n)
                if len(result) == k: # Once result reaches a size of k, we have our top K frequent elements
                    return result
