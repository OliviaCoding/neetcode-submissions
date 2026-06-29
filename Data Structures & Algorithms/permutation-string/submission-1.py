class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1_map = {}
        s2_map = {}

        for i in range(n):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
        
        if s1_map == s2_map:
            return True
        
        for right in range(n, m):
            left = right - n
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1
            s2_map[s2[left]] -= 1

            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]
        
            if s1_map == s2_map:
                return True
        
        return False