class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1 # Start with pointers at the beginning and end
        while numbers[low] + numbers[high] != target:
            if numbers[low] + numbers[high] > target:
                high -= 1 # If sum too high, move higher pointer down/left one
            else:
                low += 1 # If sum too low, move the lower pointer up/right one

        return [low + 1, high + 1]
