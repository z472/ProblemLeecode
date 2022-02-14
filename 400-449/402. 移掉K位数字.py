'''
执行用时：88 ms, 在所有 Python3 提交中击败了10.62%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了95.16%的用户

第二次过的，bug位置标记出来了。pycharm 的 bookmark第一次发现。鼠标移到上面不能显示书签内容的，很zz。
后面再看看怎么设置调整。这个题的成功提交也证实我的分析。

这题的代码我写的很慢，而且我感觉写的很糟糕。输入有num的长度到了1万。这切片一下，直接裂开。前不久有个题的超时
也是因为大量的切片。
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"

官方用个单调栈来写的，确实要更好。还有贪心的思想来保证正确性。
tc = 48ms。 sc 看了下差距不大，它用了15mb。关键是这么写，就可以非常快而且过程也少，边界判断都少。
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        1.优先级最大的是能削出小于 len(num)-k 的值，诸如 '2303502' k = 3.k比数的前置0的位数要多.
        2.遍历剩余num，从左到右，寻找下降位置，然后删除它。它的原理可以从字典序的角度和最后位数固定的角度来解释。
        '''
        frontzero = len(num.split('0')[0])
        if k >= frontzero:
            k -= frontzero
            num = str(int(num[frontzero:])) if num[frontzero:] != '' else '0'
        start = 0
        lennum = len(num)
        while k:
            for idx in range(start, lennum):
                if idx != start and num[idx] < num[idx-1]:
                    start = idx-1
                    break
            else:
                start = lennum-1
            num = num[:start]+num[start+1:]
            if num == '':
                num = '0'
            k -= 1
            lennum -= 1
            if start > 0:
                start -= 1

        return str(int(num))

mt = [( "1432219", 3), ('10200', 2), ('10', 2), ('135694', 2), ('1234', 3)]
equalt = [('1222', 2)]
bug = [('9', 1)]
for i in mt+equalt+bug:
    print(i, Solution().removeKdigits(i[0], i[1]))


