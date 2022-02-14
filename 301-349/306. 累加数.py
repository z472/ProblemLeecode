'''
执行用时：36 ms, 在所有 Python3 提交中击败了90.53%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了11.14%的用户
蛮力法，题目的输入并不大，要是很大估计会很慢。无官方题解。
提交之后感受是，难度不大，边界值很多，且有些逻辑bug。比如0。好在我的代码很有包容性，出点问题就加些条件，之前的并不影响。
'''
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        lennum = len(num)
        if lennum < 3:
            return False
        for i in range(0, lennum // 2):
            for j in range(i + 1, lennum - 1):     # bug
                if num[i + 1] != '0' or j == i+1:
                    fir, sec = int(num[:i + 1]), int(num[i + 1:j + 1])
                    idx = j+1
                    while idx < lennum:
                        x = fir + sec
                        if num[idx:idx + len(str(x))] == str(x):
                            fir, sec = sec, x
                            idx += len(str(x))
                        else:
                            break
                    else:
                        print(num[:i+1], num[i+1:j+1])
                        return True
            if num[0] == '0':
                break
        return False

mt = ["112358", "199100199", '101', '1124']
bug = ["0235813", "198019823962"]
for i in mt+bug:
    print(Solution().isAdditiveNumber(i))
