class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left, max_len = 0, 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)
            
            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len