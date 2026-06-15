class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {} # {char: count}
        left = 0
        max_len = 0

        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1

            while (right - left + 1) - max(char_map.values()) > k: # not valid
                char_map[s[left]] -= 1
                left += 1

            valid_len = right - left + 1
            max_len = max(valid_len, max_len)

        return max_len