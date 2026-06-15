class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        2. Using Hash Map
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r // 3, c // 3)]:
                    return False
                    break
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grids[(r // 3, c // 3)].add(board[r][c])

        return True


        """
        1. Brute Force

        def check(l):
            check_list = [0] * 9
            for ele in l:
                if ele != '.':
                    if check_list[int(ele) - 1] == 0:
                        check_list[int(ele) - 1] = 1
                    else:
                        return False
            return True

        def check_row(board):
            for row in board:
                if not check(row):
                    return False
            return True
        
        def check_col(board):
            for col_index in range(9):
                column = [board[row_index][col_index] for row_index in range(9)]
                if not check(column):
                    return False
            return True
        
        def check_sub_matrices(board):
            for row_start in range(0, 9, 3):
                for col_start in range(0, 9, 3):
                    sub_matrix = []
                    for i in range(3):
                        for j in range(3):
                            sub_matrix.append(board[row_start + i][col_start + j])
                    if not check(sub_matrix):
                        return False
            return True
        
        if check_row(board) and check_col(board) and check_sub_matrices(board):
            return True
        else:
            return False
        """
                    
                    
                    



