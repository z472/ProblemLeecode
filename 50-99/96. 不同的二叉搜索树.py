'''
递归版本超时，非递归版本是计算卡特兰递推式，你只是去练习编程而已。
执行用时：40 ms, 在所有 Python3 提交中击败了56.80%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了38.26%的用户
有趣的是对于小的输入，比如3非递归版本要比递归子函数还要慢一些。
官方题解给出两种复杂度的两种解法，我的属于第一个DP，它在里面详细的解释了递推式的形成，然后也和我保存的代码一样。tc=O(n^2),sc=O(n)
第二种纯卡特兰数，C(n+1)=2*(2n+1)//(n+2) * Cn    应该是化简了之类的吧，只需要一个变量来保存前一个值即可，计算式的tc为O(n),sc=1
'''

# class Solution:
#     def numTrees(self, n: int) -> int:
#         def child(mi, ma) -> int:
#             su = 0
#             if mi + 1 >= ma:
#                 return 1
#             for i in range(mi, ma):
#                 su += child(mi, i)*child(i+1, ma)
#             return su
#
#         return child(1, n+1)
# 递推式其一： C(n+1) = C0*Cn+C1*C(n-1)+C2*C(n-2)+···+Cn*C0
class Solution:
    def numTrees(self, n: int) -> int:
        res = [1, 1]
        for i in range(2, n+1):
            su = 0
            # 入栈n-1次
            for j in range(i//2):
                su += res[j]*res[(i-1)-j]
            su *= 2
            if i % 2:
                su += res[i//2]**2
            res.append(su)
        # print(res)
        return res[-1]

mt = [_ for _ in range(1,9)]
for i in mt:
    print('in:', i)
    print(Solution().numTrees(i))
# print(Solution().numTrees(5))
