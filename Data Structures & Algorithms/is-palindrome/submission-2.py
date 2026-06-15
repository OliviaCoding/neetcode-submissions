class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        2. Using Two Pointers
        """
        left, right = 0, len(s)-1
        
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left + 1, right - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        """
        1. Using Built In isalnum()
        
        filter_s = ""
        for char in s:
            if char.isalnum():
                filter_s += char.lower()
        return filter_s == filter_s[::-1]
        """
