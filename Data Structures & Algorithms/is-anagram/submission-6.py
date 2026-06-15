class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. Brute Force

        Time: O(n + m)
        n = len(s), m = len(t)

        Space: O(u)
        
        map_of_s = {}
        map_of_t = {}

        for char in s:
            map_of_s[char] = map_of_s.get(char, 0) + 1
        
        for char in t:
            map_of_t[char] = map_of_t.get(char, 0) + 1
        
        if map_of_s == map_of_t:
            return True

        else:
            return False

        """

        """
        2. Use one single hash map

        Time: O(n + m)
        n = len(s), m = len(t)
        
        Space: O(u)
        
        map_of_s = {}

        for char in s:
            map_of_s[char] = map_of_s.get(char, 0) + 1
        
        for char in t:
            if char not in map_of_s.keys():
                return False

            if map_of_s[char] == 0:
                del map_of_s[char]

            else:
                map_of_s[char] -= 1

        for count in map_of_s.values():
            if count == 0:
                return True
            else:
                return False
        """

        """
        3. Use collections.Counter

        Time: O(n + m)
        n = len(s), m = len(t)
        
        Space: O(u)

        from collections import Counter

        counter_s = Counter(s)
        counter_t = Counter(t)

        if counter_s == counter_t:
            return True
        else:
            return False
        """

        """
        4. sorted()

        Time: O(nlogn + mlogm)
        
        Space: O(n + m) 

        sorted(obj) creates a new list to contain the sorted result 
        while obj.sort() is doing inplace sorting
        """
        return sorted(s) == sorted(t)

