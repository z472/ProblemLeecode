'''
这题初见很困难，因为有未知量*号不好处理，但是括号匹配又自然想到了栈，我就萌生出一个
没有严密逻辑可以证明的算法。my:计算左右括号数量，然后计算出星号中应该包含的左右括号数量
和空字符数量。把看成左括号的星号全部视为s最左端开始出现的星号，替换，然后同理替换掉看成右
括号的星号，其间使用栈做判断。这个算法代码如下，没能通过力扣83个测试用例的最后一个。正确性
也不好证明，我这个贪心，就差合适复杂的用例来证伪。没找到就当做是正确的了，这是种不负责的糟糕
行为。再稍微理性一点就能作对了（把星号索引保存到另外的栈中，之后再稍加联想即可得到官方题解二）。

不过我看这个第83用例，化简后觉得我算法还是没问题的啊？星号按照我那么分配最后结果应为True，但
我代码结果是False。不会又是编码错误？（我是去掉该输入所有形如'()'的字符后眼睛排查，按照前面6
个为左括号，后面7后为右括号，中间1个空字符）

官方题解3的贪心优化了sc，
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        x, y = s.count('('),s.count(')')
        z = len(s)-x-y
        print(f'x={x}, y={y},z={z}')
        l = (y-x+z)//2
        r = (z-1) - l if (y-x+z)%2 else z - l
        # k是空的星号
        k = z - l -r
        if l < 0 or r < 0:
            return False
        stack = []
        print('l=', l, 'r=',r, 'k=',k)
        for idx,i in enumerate(s):
            if i == '*':
                if l > 0:
                    l -= 1
                    stack.append('(')
                if k > 0:
                    k -= 1
                elif r > 0:
                    r -= 1
                    i = ')'
            if i == '(':
                stack.append(i)
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return True if not stack else False

s = "()*()**()(())(()()(())*)()((()**))()()()(((*(((*)))(**(())))*()*))()(()()(()))()((())(*()())())()(*"
print(Solution().checkValidString(s))