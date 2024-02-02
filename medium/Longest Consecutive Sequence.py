class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # Convert to hash set for quick lookups
        longest_count = 0
        
        for n in nums:
            if (n - 1) not in nums_set: # Must be first number in its consecutive elements sequence
                curr_count = 1
                while n + curr_count in nums_set:
                    nums_set.remove(n + curr_count) # Speeds us up by removing obviously not first-in-sequence values
                    curr_count += 1 # Count length of sequence

                longest_count = max(longest_count, curr_count) # Check if longest sequence thus far

        return longest_count
