class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans
            


        '''
        Wrong solution trial
        

        nums = sorted(nums)
        ans = []
        # case 1: a + b = 0; 0 + a + b;
        for num in nums:
            if num == 0:
                left, right = 0, len(nums) - 1 
                while left < right:
                    current_sum = nums[left] + nums[right]
                    if current_sum == 0:
                        ans.append([0, nums[left], nums[right]])
                    else:
                        while current_sum > 0:
                            right -= 1
                        while current_sum < 0:
                            left += 1    
            else:
                # case 2: a + b = diff; diff = target - c
                diff = 0 - num
                left, right = 0, len(nums) - 1
                while left < right:
                    current_sum = nums[left] + nums[right]
                    if current_sum == diff:
                        ans.append([num, nums[left], nums[right]])
                    else:
                        while current_sum > diff:
                            right -= 1
                        while current_sum < diff:
                            left += 1
        return ans
        '''


        
        
            



         