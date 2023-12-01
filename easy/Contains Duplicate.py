class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nSet = set() # Hash set used for quick lookup
        for n in nums:
            if n in nSet:
                return True # If n was seen before, it means n has at least 2 instances and thus is a duplicate
            else:
                nSet.add(n) # If n was not seen before, add it to the set

        return False # No duplicates found above, thus no duplicates
