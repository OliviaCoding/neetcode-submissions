class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Using Counter
        
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
        """
        """
        2. Using Sorting

        """
        ans = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            ans[sorted_word].append(word)

        return list(ans.values())


        """
        3. Using Hash Map

        
        ans = defaultdict(list) # {tuple: list}

        for word in strs:
            count = [0] * 26 # a list for 26 distinct letters for each word in strs as a key 

            for char in word:
                count[ord(char) - ord('a')] += 1

            ans[tuple(count)].append(word) # value in the dictionary is a list so we use append here
            # key must be immutable so we cast the mutable list as immutable tuple

        return list(ans.values()) # cast the ans values as a list for output
        """

