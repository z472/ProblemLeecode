'''
执行用时：52 ms, 在所有 Python3 提交中击败了75.52%的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了54.21%的用户
官方题解：深度优先和广度优先。tc和sc都是一样的，都为O(m*n)。也是我这样从边界去发现“入口”的'O'，然后深入
进去修改能通向入口的'O'为一个别的字母用于标记，最后再遍历整个board一遍，把为'O'的给改成'X'。
'''
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 要在原地修改
        linenum, colunmnum = len(board), len(board[0])
        print(linenum, colunmnum)

        def cd(x, y):
            if board[x][y] == 'O':
                board[x][y] = 'Z'
            if x - 1 >= 0 and board[x - 1][y] == 'O':
                cd(x - 1, y)
            if x + 1 <= linenum - 1 and board[x + 1][y] == 'O':
                cd(x + 1, y)
            if y - 1 >= 0 and board[x][y - 1] == 'O':
                cd(x, y - 1)
            if y + 1 <= colunmnum - 1 and board[x][y + 1] == 'O':
                cd(x, y + 1)

            # return

        for i in range(linenum):
            for j in range(colunmnum):
                if i == 0 or i == linenum - 1 or j == 0 or j == colunmnum - 1:
                    if board[i][j] == 'O':
                        cd(i, j)

        for i in range(linenum):
            for j in range(colunmnum):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board


b1 = [['X', 'X', 'O', 'X', 'X', 'O'],
      ['O', 'X', 'O', 'O', 'X', 'X'],
      ['X', 'O', 'X', 'O', 'O', 'X'],
      ['O', 'X', 'X', 'X', 'X', 'X']]
for i in Solution().solve(b1):
    print(i)
