'''
已经看出来是纯遍历的题了，但不清楚怎么去遍历，没有好的手段能解决它。
你也清楚这种需要花，大复杂度计算的题，我力扣这么多道就没有解决过。
然后看了题解，说这是经典的 背包问题的变型。一定要掌握哦，这次一定。

题解就看：https://leetcode-cn.com/problems/ones-and-zeroes/solution/yi-he-ling-by-leetcode-solution-u2z2/

怎么说呢，它dp设的东西，就很直爽，就是要求的量。这如果不是它最后解出来了，还真的很难相信可以
这么设置。心理上的一个障碍，如果硬找个理由为啥这么设能解出来，那么可能解释就是它设置的变量的
数量是足够多的(其实应该是刚刚好)，它肯定能覆盖到这题的逻辑。 再看看它的dp表达式啊。并不普通。
看了许久吧，主要还是它 i 的理解就是刚遍历的strs的个数，这个点理解了，就好了。

那个后续优化sc，内存占用这里我觉得可以理解，因为就只是利用上一次的值嘛，sc可以缩小，但它for循环
的逆序我是一点没理解，什么“滚动数组”。可能看了经典的01背包问题就可以理解了吧。
'''