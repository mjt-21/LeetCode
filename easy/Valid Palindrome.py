class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # Two pointers; checks if string reads same left-to-right and right-to-left
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False # Not the same character, thus string not a palindrome

            l, r = l + 1, r - 1

        return True
