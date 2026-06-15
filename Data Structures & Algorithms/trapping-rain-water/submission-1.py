class Solution:
    def trap(self, height: List[int]) -> int:
        """
        2. Using Two Pointers
        """
        n = len(height)
        left, right = 0, n-1
        max_left = height[0]
        max_right = height[n-1]

        water_sum = 0
        
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(height[left], max_left)
                water_sum += max_left - height[left]
            else:
                right -= 1
                max_right = max(height[right], max_right)
                water_sum += max_right - height[right]
        return water_sum


        """
        1. Brute Force

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        max_left[0] = height[0]

        for i in range(1,n):
            max_left[i] = max(height[i], max_left[i-1])
        
        max_right[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
            
        sum = 0

        for i in range(n):
            water = min(max_right[i], max_left[i]) - height[i]
            if water > 0:
                sum += water
        
        return sum
        """


        

        