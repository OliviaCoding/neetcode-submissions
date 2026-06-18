class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # if nums[-1] > nums[0]:
        #     return nums[0]
        # else:
        #     current_min = min(nums[0], nums[-1])
        
        left, right = 0, n-1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            
            else:
                mid = (left + right) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
        
        return nums[left]
                



    