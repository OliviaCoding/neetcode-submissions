class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1_count = {}
        s2_count = {}

        for i in range(n):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        if s1_count == s2_count:
            return True
        
        for r in range(n, m):
            l = r - n

            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            s2_count[s2[l]] -= 1

            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            
            if s1_count == s2_count:
                return True
        
        return False