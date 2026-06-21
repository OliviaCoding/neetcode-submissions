class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1