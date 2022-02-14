'''
执行用时：52 ms, 在所有 Python3 提交中击败了27.18%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.24%的用户
并不难的题。居然提交错了4次。

下面是24ms代码。击败了99.9%提交。官方题解中‘槽位’，遍历一个点就占领一个槽位。
若为'#'则不开辟新槽位，若为结点则开辟两个槽位（因为它就算是有空也是一个槽位）。
若最后槽位为0则正确，否则都错误。   下面代码就是完美诠释。

sc 不只是 sc:
    它虽然是tc=O(N)和我一样，但是由于sc=O(1)远远小于我的 N 的队列。故它没有对数据结构的操作的时间。
    是不是可以理解，tc相同时，sc仍会严重影响速度。sc也是tc的一个重要指标。

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        res=1
        for i in preorder.split(','):
            res-=1
            if res<0:
                return False
            if i!='#':
                res+=2
        return res==0

'''
from collections import deque
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 8行初始化， 11行循环逻辑
        preorder = preorder.split(',')      # bug:1
        lenstr = len(preorder)
        if preorder == ['#']:
            return True
        if lenstr < 3:
            return False
        i = 1
        d1 = deque([preorder[0]])
        lend1 = 1
        while d1[0] != '#':     # bug:3
            if lend1 > 2 and d1[-2] == d1[-1] == '#':
                lend1 -= 2
                d1.pop()
                d1.pop()
                d1[-1] = '#'
            elif i < lenstr:
                d1.append(preorder[i])
                lend1 += 1
                i += 1
            else:
                return False
        return True if i == lenstr else False   # bug:1

mt = ["9,3,4,#,#,1,#,#,2,#,6,#,#", "1,#", "9,#,#,1", ]
bugF = ["1,#,#,#,#", "#,#,#"]
bugT = ["9,#,92,#,#", '#', ]
for i in mt[:]+bugT[:]+bugF[:]:
    print(i, '->', Solution().isValidSerialization(i))
