'''
tc > 94%, sc > 96%。惊人的分治算法。这算法是基于一个分析，就是如果把某一个运算符的看作一个中断或者说
是一系列解的标志。这是它无重复解的原因。然后分别算左右两边的值并做笛卡尔积。
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res
'''
from typing import List


class Solution:
    # DP有漏解，漏的还不少，主要还是存在 后续性。
    def diffWaysToCompute(self, exp: str) -> List[int]:
        lenexp = len(exp)
        if lenexp == 1:
            return [int(exp)]
        pretwo = [exp[0]]
        preone = [str(eval(exp[:3]))]
        cou = 0
        for i in range(4, lenexp, 2):
            x = exp[i - 1:i + 1]
            sav = preone
            preone = [str(eval(s + x)) for s in preone]
            y = str(eval(exp[i - 2:i + 1]))
            pretwo = [str(eval(s + exp[i - 3] + y)) for s in pretwo]
            preone = preone + pretwo
            pretwo = sav
            print(cou, ':', preone, pretwo)
            cou += 1
        preone = [int(i) for i in preone]
        return preone


mt = ["2*3-4*5", '2-1-1']
print(mt[0])
for i in mt[:1]:
    print(i, Solution().diffWaysToCompute(i))
