class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterS = {}
        letterT = {}

        for char in s:
            if char.isalpha():
                if char in letterS:
                    letterS[char] += 1
                else:
                    letterS[char] = 1

        for char in t:
            if char.isalpha():
                if char in letterT:
                    letterT[char] += 1
                else:
                    letterT[char] = 1

        return (letterS == letterT)   