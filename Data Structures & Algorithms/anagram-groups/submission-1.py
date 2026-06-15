class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Using Counter
        """
        from collections import Counter

        if len(strs) == 1:
            return [[strs[0]]]

        ans = []
        
        for word in strs:
            found = False

            for group in ans:
                if Counter(word) == Counter(group[0]):
                    group.append(word)
                    found = True
                    break

            if not found:
                ans.append([word])

        return ans
