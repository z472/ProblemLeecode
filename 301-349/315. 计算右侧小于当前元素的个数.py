'''
执行用时：2152 ms, 在所有 Python3 提交中击败了62.22%的用户
内存消耗：43.4 MB, 在所有 Python3 提交中击败了14.33%的用户
困难题，看的题解中的 归并排序 的改写方法实现的。分治方法的又一个经典题。这里虽然是用返回的左右
子序列。但其实很重要的理解算法的点就是 右半区会为左半区服务，更新的ans（全局返回列表）也是更新
左半区的。第二点就是归并排序，是分到底层1个1个的，然后再 合并 起来的。它右边的半区其实就是已经
处理好的。所以它是正确的。

归并排序：tc = O(nlogn), sc = O(n)。 返回合并时期才开始计算时间复杂度。 nlogn 可以说是最坏的情况。
稳定性：稳定排序。
缺点：空间占用大，要分治递归。
优点：仅次于快速排序。高效。

这道题用归并排序思想做的事要多一些。要绑定值与返回值列表的索引。多了一点东西。
'''
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        assit = list(enumerate(nums))

        def mergesort(ijlist):
            '''
            itype: List[tuple(int, int)]
            rtype: List[tuple(int, int)]
            '''
            lenij = len(ijlist)
            if lenij == 1:
                return ijlist
            left = mergesort(ijlist[:lenij//2])
            right = mergesort(ijlist[lenij//2:])
            ret = []
            p1, p2 = 0, 0
            while p1 < lenij//2 and p2 < lenij - lenij//2:
                i = left[p1]
                if i[1] > right[p2][1]:
                    ret.append(right[p2])
                    p2 += 1
                else:
                    p1 += 1
                    ret.append(i)
                    ans[i[0]] += p2

            for j in range(p1, lenij//2):
                ans[left[j][0]] += p2
            ret += left[p1:]
            ret += right[p2:]
            return ret

        mergesort(assit)
        return ans

mt = [[5,2,6,1], [5]]
for i in mt:
    print('input:', i, '-> ', Solution().countSmaller(i))





