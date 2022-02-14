'''
感觉这个无法成功了，在力扣1800个测试中，通过了1707个，卡在一个超长的测试用例上，然后是超时了。
'''
class Solution:
    def isMatch(self, s, p):
        # s: str, p: str) -> bool
        ind_s, tag = 0, 0     # tag 1 可遍历s，tag 0不可，另两个为索引
        for idx, i in enumerate(p):
            if i == '*':
                tag = 1
            elif i == '?':
                ind_s += 1
            else:
                if tag == 1:
                    for jdx, j in enumerate(s):
                        if jdx >= ind_s and j == i and self.isMatch(s[jdx:], p[idx:]):
                            return True
                    return False
                else:
                    if ind_s > len(s)-1 or s[ind_s] != i:     # 条件的顺序不能反过来
                        return False
                    ind_s += 1
                    tag = 0
        if s == '' or p == '':
            if p == '':
                return False if s != p else True
        if ind_s > len(s):
            return False
        elif ind_s == len(s) or tag == 1:
            return True
        else:
            return False

a = Solution()
mytest1 = [('aa', '*??'), ('aa', '??'), ('aa', '???*'),]
mytest2 = [('accbjkcdbc', 'a*k?dbc'), ('cv', '?c'), ('cb', 'c?b'), ('acdcb', 'a*d?b')]     # ('acdcb', 'a*c?b')
lee_test = [('accbjkcdbc', 'a*bc'), ('', 'c'), ('', '***?'), ("bbbaba", "bb**??"), ('bbbaba', '*??')]
for i in mytest2:
    print('空' if i[0] == '' else i[0], ' ', i[1])
    print(a.isMatch(i[0], i[1]))