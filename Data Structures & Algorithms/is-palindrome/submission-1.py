class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. Using Built In isalnum()
        """
        filter_s = ""
        for char in s:
            if char.isalnum():
                filter_s += char.lower()
        return filter_s == filter_s[::-1]