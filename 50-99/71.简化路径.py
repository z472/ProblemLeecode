'''
    执行用时：44 ms, 在所有 Python3 提交中击败了52.15%的用户
    内存消耗：14.7 MB, 在所有 Python3 提交中击败了58.23%的用户
    一次过，测试数据做的不错。
    改良版栈：本来可以把列表当做一个栈来实现的，但是如果是pop(-1)的话
    对于列表的修改时O(n)复杂度，我就设置个end变量表示列表中最后一个非''字符
    串的位置，出栈就是把列表end位置的值改成''，当然还有其他情况。增加还是用的
    append方法。
    官方题解：无，一个py3的提交，
    执行用时: 36 ms , 在所有Python3 提交中击败了94.49% 的用户
    内存消耗: 13.6 MB , 在所有Python3提交中击败了72.47% 的用户
    class Solution:
    def simplifyPath(self, path: str) -> str:
        pl = [p for p in path.split('/') if p not in ['','.']]
        while '..' in pl:
            idx = pl.index('..')
            if idx != 0:
                pl = pl[:idx-1] + pl[idx+1:]
            else:
                pl.remove('..')
        return '/' + '/'.join(pl)
    它的pl预处理写的确实不错，但是后面的又是index，又是切片，又是
    remove的竟然能比我快占用还少，懒人写法比我快？！看完我像个小丑。。。麻了

    相关知识str.split(sep=None, maxsplit=-1)
    返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。
    如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。
    如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）。
'''
class Solution:
    def simplifyPath(self, path):
        # path: str) -> str:
        # 存除了..和.的所有东西，然后再整合起来
        res = [None]
        sav = ''
        end = -1
        for i in path+'/':
            if i == '/' and sav:
                if sav == '..':
                    if end >= 0:
                        print('出栈：', res[end])
                        res[end] = ''
                        print('--', res)
                        if end >= -1:
                            end -= 1
                elif sav != '.':
                    if not res[-1]:
                        print('入栈1：', sav)
                        res[end+1] = sav
                        print('--', res)
                    else:
                        res.append(sav)
                        print('入栈2：', sav)
                        print('--', res)
                    end += 1
                sav = ''
            else:
                if i != '/':
                    sav += i
        print('res:', res, 'end=', end)
        if not res[end]:
            return '/'
        return '/'+'/'.join(res[:end+1])

a = Solution()
leet = ["/home", "/../../a", "/home//foo", "/a/./b/../././../c", '/..']
mt = ['///./a/b/c/d/../../....', ]
for i in leet:
    print('in:', i)
    print(a.simplifyPath(i))