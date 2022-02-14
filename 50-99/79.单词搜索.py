'''
执行用时：320 ms, 在所有 Python3 提交中击败了16.93%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了43.65%的用户
第二次过的这个表现，我觉得已经不错了，我以为会超时呢，它测试的输入的word长度最长是10^3，而且我第一错错在word长度为1的输入上面，改bug并没有
花太多时间。用CSGO的术语就是短痛。这题我是蛮力法+蛮写，子函数的代码很容易错很长，而且出口很多（也没办法就是有那么多情况）。

官方题解：
'''
class Solution:
    def exist(self, board, word):
        # board: List[List[str]], word: str) -> bool:
        sav = [0] * len(word)
        d1 = {}

        def child(k):
            x, y, tag = sav[k - 1][0], sav[k - 1][1], 0
            for i in range(4):
                # 向左，向右，向上，向下，排除在之前sav中的坐标（高耗时），排除该位置不等于预期的字符
                if i == 0 and x - 1 >= 0 and board[x - 1][y] == word[k] and y not in d1.get(x - 1, []):
                    sav[k], tag = (x - 1, y), 1
                    if d1.get(x - 1):
                        d1[x - 1].append(y)
                    else:
                        d1[x - 1] = [y]
                elif i == 1 and x + 1 < len(board) and board[x + 1][y] == word[k] and y not in d1.get(x + 1, []):
                    sav[k], tag = (x + 1, y), 2
                    if d1.get(x + 1):
                        d1[x + 1].append(y)
                    else:
                        d1[x + 1] = [y]
                elif i == 2 and y + 1 < len(board[0]) and board[x][y + 1] == word[k] and y + 1 not in d1.get(x, []):
                    sav[k], tag = (x, y + 1), 3
                    d1[x].append(y + 1)
                elif i == 3 and y - 1 >= 0 and board[x][y - 1] == word[k] and y - 1 not in d1.get(x, []):
                    sav[k], tag = (x, y - 1), 4
                    d1[x].append(y - 1)

                if tag == i + 1:
                    if k == len(word) - 1:
                        return True
                    else:
                        if child(k + 1) == 1:
                            return True
                        if tag == 1:
                            d1[x - 1].remove(y)
                        elif tag == 2:
                            d1[x + 1].remove(y)
                        elif tag == 3:
                            d1[x].remove(y + 1)
                        else:
                            d1[x].remove(y - 1)
                            return False
                elif i == 3:
                    return False

        for ix in range(len(board)):
            for iy in range(len(board[0])):
                if board[ix][iy] == word[0]:
                    sav[0] = (ix, iy)
                    d1[ix] = [iy]
                    if len(word) == 1:
                        return True
                    elif child(1) == 1:
                        print('sav:', sav)
                        return True
                    else:
                        d1[ix].remove(iy)
        print('sav:', sav)
        return False

a = Solution()
board1 = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
mt = ('ABCCED', 'SEE', 'ABCD', 'F')
for j in board1:
    print('\t', j)
for i in mt:
    print('word:', i)
    print('output:', a.exist(board1, i))