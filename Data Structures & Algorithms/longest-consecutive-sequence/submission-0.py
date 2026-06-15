class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = sorted(set(nums))
        max_con = 1
        count = 1

        for i in range(len(nums)-1):
            if (nums[i+1] - nums[i]) == 1:
                count += 1
                max_con = max(count, max_con)
            else:
                count = 1
                continue

        return max_con

            