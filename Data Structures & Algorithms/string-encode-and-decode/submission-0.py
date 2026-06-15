class Solution:

    #["neet","code","love","you"] -> 4#neet4#code4#love3#you -> ["neet","code","love","you"]

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans = ans + str(len(s)) + '#' + s
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        # pointrt i for the beginning of each word; pointer j for each letter in each word
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j]) # s[j-1]
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
            

        return ans
