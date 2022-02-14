'''
看了下题解，发现是数学的分析不足够，可以偷懒的，只有加减运算，括号没有优先级，没必要特殊处理。
'''
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []

        def calculate_bracket(entrance: int) -> (int, int):
            # 入口参数是该左括号在s中的索引，返回一个括号中式子的值和该左括号对应的右括号的索引
            ret = s[entrance+1]
            while True:



        calculate_bracket()


Solution().calculate('d')
