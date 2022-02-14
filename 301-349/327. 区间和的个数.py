'''
官方题解法一：优化O(N^2)+归并排序
    在知道了N^2算法，设前缀和数组p。

    它首先把问题降低难度，考虑两个升序数组。然后又用类似平方算法的
    遍历方式，先确定一个p[0]然后向右寻找两次分别确定p[i] >= p[0]+lower 和 p[j] > p[0]+upper
    那样从 i —— j-1就是合法的对于p[0]的序列和。之后它p[0] 变成了从 p[1]开始。由于p[1]>p[0]。故
    之前的i 和 j只向后遍历即可。重复这个过程，复杂度为O(N)。

    然后是回归本题。它的原话没全懂，也没py3代码。
        我们采用归并排序的方式，能够得到左右两个数组排序后的形式，以及对应的下标对数量。对于原数组而言，
        若要找出全部的下标对数量，只需要再额外找出左端点在左侧数组，同时右端点在右侧数组的下标对数量
'''