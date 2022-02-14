'''
执行用时：68 ms, 在所有 Python3 提交中击败了5.01%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.05%的用户
第一次超时了，嗯确实很糟糕的编码体验。写的也很慢，bug频发。
官方题解：
好多方法都是先把头尾空格去掉。嗯。。
1.class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
40ms, 15.1MB 74% 16%

2.整体翻转，保留一个空格，然后局部翻转。主要是给C++语言的字符串是可变的。
py3看他写了好几个函数很麻烦。

3.用一个队列来存储，获取一个单词就加在左边。
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        le = len(s)
        def cd(begin):
            sbegin, send = -1, 0
            for i in range(begin, le):
                if s[i] != ' ':
                    if sbegin < 0:
                        sbegin = i
                else:
                    if sbegin >= 0:
                        send = i
                        break
            if send == 0 and sbegin >= 0:
                return s[sbegin:]
            elif send != 0:
                return cd(send) + ' ' + s[sbegin:send]
            else:
                return ''

        s = cd(0)
        return s[1:] if s[0] == ' ' else s

mt = ["a good   example", "  Bob    Loves  Alice   ", "Alice does not even like bob", ]
for i in mt:
    print('in:', repr(i))
    print(repr(Solution().reverseWords(i)))