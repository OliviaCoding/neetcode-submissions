class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]: # target is in the bottom part, moving down
                top = mid_row + 1
            elif target < matrix[mid_row][0]: # target is in the top part, moving up
                bot = mid_row - 1
            else: # found the possible target row, matrix[mid_row][0] <= target <= matrix[mid_row][-1]
                break
        
        if not (top <= bot): # didn't find the target row
            return False
        
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid_row][mid]: # target is on the left, moving left
                right = mid - 1
            elif target > matrix[mid_row][mid]: # target is on the right, moving right
                left = mid + 1
            else: # target == matrix[mid_row][mid]
                return True
        
        return False # didn't found it


