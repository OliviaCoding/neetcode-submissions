class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            left, right = 0, cols - 1

            if matrix[r][left] <= target <= matrix[r][right]:
                while left <= right:
                    mid = left + (right - left) // 2

                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                return False
        
        return False

