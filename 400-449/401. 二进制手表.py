'''
执行用时：44 ms, 在所有 Python3 提交中击败了57.71%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了32.59%的用户

这居然算是简单题，我在递归逻辑那里先是没考虑0，无限递归了，然后又是当restone为0时的返回值出错，导致返回值出错。
后面就没bug了，还好。提交也是一次过的。
'''
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def cd(restone, restplace):
            if restone == restplace:
                return [(1 << restplace) - 1]
            elif restone > 0:
                ret = [(i << 1) + 1 for i in cd(restone - 1, restplace - 1)]
                if restone < restplace:
                    ret += [i << 1 for i in cd(restone, restplace - 1)]
            else:
                ret = [0]
            return ret

        ans = []
        minhour = turnedOn - 6 if turnedOn - 6 > 0 else 0
        maxhour = turnedOn if turnedOn < 4 else 4
        for hour in range(minhour, maxhour + 1):
            x, y = cd(hour, 4), cd(turnedOn - hour, 6)
            for i in x:
                for j in y:
                    if j < 60 and i < 12:
                        if j < 10:
                            ans.append(str(i) + ':0' + str(j))
                        else:
                            ans.append(str(i) + ':' + str(j))
        return ans


mt = [1, 2, 0]
for i in mt:
    print('turnedOn:', i)
    print(Solution().readBinaryWatch(i))
    print()
