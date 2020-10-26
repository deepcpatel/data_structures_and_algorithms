# Link: https://leetcode.com/problems/valid-sudoku/

# Approach: Create three list of 9 hash sets. First list keep track of all number in all rows, second list keep track of all numbers in all columns and third list keep track of
# all nine (3x3) blocks. Then run a nested loops iterating all cells of sudoku and see whether the number is encountered before in all three lists. To map 3x3 blocks, use formula
# in line 18.


class Solution(object):
    def isValidSudoku(self, board):
        row_set = [set([]) for i in range(9)]   # 9 rows each having a hash set to record numbers in them
        col_set = [set([]) for i in range(9)]   # 9 columns each having a hash set to record numbers in them
        blk_set = [set([]) for i in range(9)]   # 9 (3x3) blocks each having a hash set to record numbers in them
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])     # Getting number
                    blk_idx = (i//3)*3 + j//3  # Mapping (3x3) block index in blk_set based on i and j
                
                    if (num in blk_set[blk_idx]) or (num in row_set[i]) or (num in col_set[j]):
                        return False
                    else:
                        blk_set[blk_idx].add(num)
                        row_set[i].add(num)
                        col_set[j].add(num)
        return True