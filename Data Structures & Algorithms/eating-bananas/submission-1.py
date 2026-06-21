class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left, right = 1, max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            t_sum = 0

            for p in piles:
                t_sum += math.ceil(p/mid)

            if t_sum > h:
                left = mid + 1
            else:
                right = mid

        return left




        