'''
执行用时：60 ms, 在所有 Python3 提交中击败了17.05%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了90.57%的用户
通过测试用例：63 / 63

纯纯是编码题，不需要分析思考。
看下官方的实现：
class Solution(object):
    def letterCasePermutation(self, S):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))

'''
from itertools import product
from functools import reduce
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        x = [(i,) if '0'<=i<='9' else (i,i.upper()) if 'a'<= i <= 'z' else (i,i.lower()) for i in s]
        return [reduce((lambda x,y:x+y),i)  for i in product(*x)]

test = ['a1C2d3']
for i in test:
    print(Solution().letterCasePermutation(i))