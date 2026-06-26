class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in s_map:
                left = max(s_map[s[right]] + 1, left)
            
            s_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
