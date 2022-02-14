from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sav = [0] * k
        ret = []
        remainvalue = n

        def cd(idx: int, start: int):
            nonlocal remainvalue
            if remainvalue < start:
                return False
            if idx < k - 1:
                for i in range(start, 10):
                    sav[idx] = i
                    remainvalue -= i
                    if i != 9:
                        cd(idx + 1, i + 1)      # 剪枝失败，出了回溯过多的bug
                    remainvalue += i
            elif remainvalue < 10:
                sav[idx] = remainvalue
                if sav not in ret:
                    ret.append(sav[:])
            return True

        invalue = n - (20 - k) * (k - 1) // 2
        invalue = 1 if invalue <= 0 else invalue
        for i in range(invalue, 10):
            remainvalue = n
            cd(0, i)
        return ret


mt = [(3, 7), (3, 9), (3, 17)]
bug = [(2,6), (4,24)]
for i in bug:
    print('k=%d n=%d' % (i[0], i[1]), end='--->')
    print(Solution().combinationSum3(i[0], i[1]))

print('(4, 24)\n',[[1,6,8,9],[2,5,8,9],[2,6,7,9],[3,4,8,9],[3,5,7,9],[3,6,7,8],[4,5,6,9],[4,5,7,8]])