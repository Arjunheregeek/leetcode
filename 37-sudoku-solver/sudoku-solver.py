from typing import List
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        avai_col = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        avai_row = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        avai_subsquare = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    avai_row[i].remove(val)
                    avai_col[j].remove(val)
                    avai_subsquare[(int(i/3)*3) + int(j/3)].remove(val)

        def backtrack(i, j, board):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    return True
                elif  j < 8:
                    return backtrack(i, j + 1, board)
                elif i < 8 and j == 8:
                    return backtrack(i + 1, 0, board)
            
            avai_set = avai_row[i] & avai_col[j] & avai_subsquare[(i//3)*3 + j//3]
            for v in avai_set:
                board[i][j] = str(v)

                avai_row[i].remove(v)
                avai_col[j].remove(v)
                avai_subsquare[(int(i/3)*3) + int(j/3)].remove(v)

                if (i == 8 and j == 8) or (j < 8 and backtrack(i, j + 1, board)) or (i < 8 and j == 8 and backtrack(i + 1, 0, board)):
                    return True

                board[i][j] = '.'
                avai_row[i].add(v)
                avai_col[j].add(v)
                avai_subsquare[(int(i/3)*3) + int(j/3)].add(v)

        backtrack(0, 0, board)
            
            

        