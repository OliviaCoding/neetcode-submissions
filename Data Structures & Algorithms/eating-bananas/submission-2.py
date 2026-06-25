class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            time_sum = 0
            mid = left + (right - left) // 2

            for p in piles:
                t = math.ceil(p / mid)
                time_sum += t
            
            if time_sum <= h:
                right = mid
            else:
                left = mid + 1
        
        return left