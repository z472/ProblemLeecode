'''
执行用时：28 ms, 在所有 Python3 提交中击败了89.94%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.16%的用户
通过测试用例：109 / 109

这题特殊情况很多，wrong测试组的个数 <= 提交失败次数。对了，如果dp数组的遍历顺序为斜向遍历，可以把二维dp
改写为一维dp，可以再优化下。     下面官方题解代码：

class Solution:
    def win(self, board: List[str], p: str) -> bool:
        return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                   board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
                   board[0][0] == p and board[1][1] == p and board[2][2] == p or \
                   board[0][2] == p and board[1][1] == p and board[2][0] == p

    def validTicTacToe(self, board: List[str]) -> bool:
        oCount = sum(row.count('O') for row in board)
        xCount = sum(row.count('X') for row in board)
        return not (oCount != xCount and oCount != xCount - 1 or
                    oCount != xCount and self.win(board, 'O') or
                    oCount != xCount - 1 and self.win(board, 'X'))

它的return判断逻辑其实没什么关系，主要还是把那些wrong的特殊情况，考虑到了。这种写法也值得学习哦，any函数我用的
不多。它和写法相比它把玩家获胜的情况更清楚的写到了win中，它要遍历两次，我是把玩家获胜写到了变量tagxo中，我只遍历
一次。
'''
from functools import reduce
from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        t = ''.join(reduce((lambda x, y: x + y), board))
        x, o = t.count('X'), t.count('O')
        dp = [[(1, 1) for _ in range(3)] for _ in range(3)]
        tagxo = 0
        def jud(a,b):
            if (tagxo == 1 and board[a][b] == 'O') or (tagxo == 2 and board[a][b]=='X'):
                return 3
            return 1 if board[a][b] == 'X' else 2

        for i in range(3):
            for j in range(3):
                left, up = 1, 1,
                if j > 0 and board[i][j] == board[i][j - 1] != ' ':
                    left = dp[i][j - 1][0] + 1
                if i > 0 and board[i][j] == board[i - 1][j] != ' ':
                    up = dp[i - 1][j][1] + 1
                dp[i][j] = (left, up)
                if 3 in dp[i][j]:
                    tagxo = jud(i,j)
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            tagxo = jud(0,0)
        elif board[0][2] == board[1][1] == board[2][0] != ' ':
            tagxo = jud(1,1)
        for _ in range(3):
            print(dp[_])
        print(f'tagxo={tagxo}')
        if tagxo == 3: return False
        if tagxo == 2: return x == o
        if tagxo == 1: return x == o + 1
        return x == o or x == o + 1

test = [["XOX"," X ","   "], ["XXX","   ","OOO"], ["XOX","O O","XOX"]]
wrong = [["   ","   ","   "], ["OOO","XXO","XXX"],["XXX","OOX","OOX"]]
for i in test+wrong:
    print(f'i={i}\n', Solution().validTicTacToe(i),'\n')
