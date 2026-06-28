class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        s1_count = {}
        s2_count = {}

        for i in range(n):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        if s1_count == s2_count:
            return True
        
        for right in range(n, m):
            left = right - n

            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
        
            if s1_count == s2_count:
                return True
        
        return False