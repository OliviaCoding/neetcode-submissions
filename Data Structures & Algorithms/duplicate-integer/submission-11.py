class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Brute force:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                    if nums[i] == nums[j]:
                        return True
        return False

        """
        """
        Using data structure: set()
        """
        unique_nums = set(nums)

        if len(nums) == len(unique_nums): # No duplicate
            return False
        else: # We do have duplicate
            return True
        

       
