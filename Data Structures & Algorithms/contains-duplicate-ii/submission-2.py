class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_set = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] in seen_set:
                return True
            
            seen_set.add(nums[right])

            if len(seen_set) == k + 1:
                seen_set.remove(nums[left])
                left += 1
            
        return False