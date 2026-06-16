class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1

        while left < right:
            while left < right and not self.isAlNum(s[left]):
                left += 1

            while left < right and not self.isAlNum(s[right]):
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            
            else:
                return False
                

        return True
    
    def isAlNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    