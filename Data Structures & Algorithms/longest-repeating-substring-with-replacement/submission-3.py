class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre_map = {}
        left, max_len, max_fre = 0, 0, 0

        for right in range(len(s)):
            fre_map[s[right]] = fre_map.get(s[right], 0) + 1
            max_fre = max(max_fre, fre_map[s[right]])

            if (right - left + 1) - max_fre > k:
                fre_map[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
  
        return max_len

