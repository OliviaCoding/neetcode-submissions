class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_len, max_fre = 0, 0, 0
        count_map = {}

        for right in range(len(s)):
            count_map[s[right]] = count_map.get(s[right], 0) + 1
            max_fre = max(max_fre, count_map[s[right]])

            if (right - left + 1) - max_fre > k:
                count_map[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

            
            
