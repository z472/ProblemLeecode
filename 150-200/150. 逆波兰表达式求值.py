'''
执行用时：100 ms, 在所有 Python3 提交中击败了17.54%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了46.69%的用户
一次过，偷懒的写法。下面的写法40ms，差太多了吧。
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                v1 = int(st.pop())
                v2 = int(st.pop())
                if tokens[i] == '+':
                    st.append(v1+v2)
                elif tokens[i] == '-':
                    st.append(v2-v1)
                elif tokens[i] == '*':
                    st.append(v1*v2)
                else:
                    st.append(v2/v1)
            else:
                st.append(tokens[i])

        return int(st[0])
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['-', '+', '*', '/']
        for i in tokens:
            if i in operator:
                x = int(eval(stack[-2] + i + stack.pop()))
                stack[-1] = str(x)
            else:
                stack.append(str(i))

        return int(stack[0])

mt = [["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]
for i in mt[:]:
    print('in:', i)
    print(Solution().evalRPN(i))
