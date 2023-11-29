class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nSet = set() # set simply used for quick lookup, checking if each number was seen before
        for n in nums:
            if n in nSet:
                return True # if n was seen before, it means n has at least 2 instances and thus is a duplicate
            else:
                nSet.add(n) # if n was not seen before, add it to the set
