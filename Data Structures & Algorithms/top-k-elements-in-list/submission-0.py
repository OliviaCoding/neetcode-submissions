class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Brute Force: Using Hash Map
    
        """
        num_dict = {}

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        sorted_dict_by_values = {k: v for k, v in sorted(num_dict.items(), key = lambda item:item[1], reverse = True)}
        

        return list(sorted_dict_by_values.keys())[:k]

