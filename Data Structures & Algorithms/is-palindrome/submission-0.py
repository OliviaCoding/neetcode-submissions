class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_chars = [char.lower() for char in s if char.isalnum()]

        return filter_chars == filter_chars[::-1]