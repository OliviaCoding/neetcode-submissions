class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        2. Prefix and Postfix

        """
        ans = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans

        
        """
        1. Brute Force
       
        n = len(nums)
        ans = []

        for i in range(n):
            prod = 1

            for j in range(n):
                if i != j:
                    prod *= nums[j]
                else:
                    continue
            ans.append(prod)

        return ans
         """
