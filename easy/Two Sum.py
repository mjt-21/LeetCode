class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {} # Key is a number, value is the number's index
        for i in range(0, len(nums)):
            if target - nums[i] not in numsHash.keys(): # Working "backwards" in a sense, target - nums[i] is the value we need to sum to target
                numsHash[nums[i]] = i # If we can't find the needed value, add the current value to the hash table and try again
            else:
                return [i, numsHash[target - nums[i]]] # If we do find the needed value, return the indexes of the current value and the matching value
