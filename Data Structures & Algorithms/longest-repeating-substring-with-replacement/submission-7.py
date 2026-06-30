class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen_map = {}
        left, max_fre, max_len = 0, 0, 0

        for right in range(len(s)):
            seen_map[s[right]] = seen_map.get(s[right], 0) + 1
            max_fre = max(max_fre, seen_map[s[right]])

            if (right - left + 1) - max_fre > k:
                seen_map[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len