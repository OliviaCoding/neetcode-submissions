class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

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
                    
                    
                    



