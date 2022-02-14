'''
力扣的官方解法为：一次遍历，针对81个位置，建立行、列、单元三个列表（每个里面是字典）
'''
class Solution:
    def findduplicate(self, list9):
        for i in range(9):
            if list9[i] != '.':
                j = i+1
                while j <= 8:
                    if list9[i] == list9[j]:
                        return False
                    else:
                        j += 1
        return True

    def isValidSudoku(self, board):        # board: List[List[str]]  return : bool(true or false)
        for i in range(9):
            if not self.findduplicate(board[i]):
                return False
        l9 = ['.' for _ in range(9)]
        for i in range(9):
            for j in range(9):
                l9[j] = board[j][i]
            if not self.findduplicate(l9):
                return False
        for i in range(1, 10):
            for j in range(3):
                l9[j*3:j*3+3] = board[( (i-1)//3 )*3+j][((i-1)%3)*3:((i-1)%3)*3+3]
            # print(l9)
            if not self.findduplicate(l9):
                return False
        return True

t1 = (["5","3",".",".","7",".",".",".","."], )
t2 = ([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
], [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])
a = Solution()
for i in t2:
    print('result:', a.isValidSudoku(i))
# print(a.findduplicate(t2[0][0]))
'''
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True
'''