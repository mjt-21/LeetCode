class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) # Using some trickiness to not need a separate "prefix" and "postfix" array later; simply calculating them within this result list as we go along

        prefix = 1
        for i in range(len(nums)): # Left to right
            result[i] = prefix # Sets i'th element of result to its prefix product
            prefix *= nums[i] # Calculates prefix value as it goes along

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Right to left
            result[i] *= postfix # Sets i'th element of result to be prefix times postfix, aka the product of the array except itself!
            postfix *= nums[i] # Calculates postfix value as it goes along
        
        return result
