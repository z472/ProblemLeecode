'''
这道题没有去推dp，倒是有个dfs递归的想法，看了官方题解的dp解释，完完全全就是我递归的反向操作。
因为这题是统计最小操作次数，所以不能直接计算得出，就是要算各种情况，然后得出一个最小值。
分析只能复制cur值和粘贴上一个复制的值last，就是最后n这个数字必定是粘贴，和它上一步的复制操作
可以得到，这个n是由n//last个的last组成(粘贴而成的)。这就是dp表达式，但我要写就是用记忆化dfs。
这题dfs感觉和dp是没有时间效率什么的区别的，完全的正反两个流程。

官方第二种是 分解质因数，tc更小，有时间看下。
'''