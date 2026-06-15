class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        left = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            current_count = right - left + 1
            max_count = max(max_count, current_count)
        return max_count