print('''不足很多，思路上就很狭窄，然后是需要特别靠列表来做，遍历的时候用字典不方便，但是在寻找匹配括号下一个的时候
 又需要字典映射的功能，要不就是我第一个循环中的子遍历。然后又针对输出rtol来做的算最长算法，给自己又挖了个题出来。所有情况看似都处理好了。
 网站的一个用例'()(())'又迫使你处理一遍rtol，把被别人包含的括号都配合计算最长来改变i[1]。 ''')
print('''总结：过程有点长，分个个步骤看似有条不紊，但实际并没有怎么化简问题，产生的子问题仍然难于处理。
            算法思想限制你的操作，我的算法是：从左向右遍历找到一个右括号，然后向左遍历寻找和它匹配的左括号，
            如果不存在就视为---中断，以元组的形式存在rtol列表中。如果右括号的左边是一个右括号就跳到和他匹配的左括号的左边，
            如果右括号是个中断的，那么当前右括号为中断。用rtol列表来存一段一段的有效括号。然后是把包含的子括号元组给标记为中断，
            计算最长的时候就会好处理很多，有几种情况。''')
print('''编程的收获：一是：不要有不可控的代码，每行都要表意明确，不明确的代码日后续写或是修改会非常头晕。
            我第二天改昨天的第一个循环理解了半天昨天的思路。不同情况相同处理也要先分开写，然后观察整合。
            二是：以事实为算法设计时的基础，不要自己空想，空想出的东西很容易成为废品
            三是：这个算法在力扣里是既慢又占空间，并不好。原因可能是多次的添加元素，python list添加时O（n）。''')
class Solution:
    def longestValidParentheses(self, s):   # return int
        rtol = []
        for idx, i in enumerate(s):
            if i == ')':
                left = idx-1
                if s[idx-1] != '(':
                    a = -1
                    while left >= 0:        # 边界值判断作用
                        left = rtol[a][1]-1
                        if left < 0 or s[left] == '(':
                            break
                        while rtol[a][0] != left:
                            a -= 1
                rtol.append((idx, left))
        print('rtol:', rtol)
        max_len, right, sumi =0, None, 0
        for idx, i in enumerate(rtol):
            jdx = idx+1
            while jdx < len(rtol) and rtol[jdx][1] >= 0:
                if rtol[jdx][1] < i[1]:
                    rtol[idx] = (i[0], -77)
                    break
                jdx += 1
        print(rtol)
        for i in rtol:
            if i[1] >= 0:
                if not right:
                    max_len = i[0]-i[1]+1
                    sumi = max_len
                elif i[1]-right==1:
                    sumi += i[0]-i[1]+1
                else:
                    sumi = i[0]-i[1]+1
                max_len, right = max(sumi, max_len), i[0]
                # print(max_len,'  ',right,'   ',sumi)
        return max_len

a = Solution()
test = ['()((()', '()(()', '())())((())())', '()(()(()()()', '())((())()))))', ')', ')(', ')))', ]
test2 = ['()(())', ]
for i in test2[:]:
    print('_______\n', i)
    print(a.longestValidParentheses(i))



