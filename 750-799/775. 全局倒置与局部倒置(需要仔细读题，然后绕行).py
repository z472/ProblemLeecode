'''
这题目的意思是全局倒置会包含部分倒置，让我们判断二者数目是否相等，就是判断有没有逆序对只存在于全局倒置中。
整个的解法就出现了变化。        我初始的理解是让我分别求两个倒置的个数，然后比较呢。我知道部分倒置的个数
就是白给，很奇怪呢怎么会要求这么简单的东西。      这题主要考察的是，能否通过对数据相互关系的特点，来降低
题的难度。这是很常见的手法，经常会有这种题是要求b值，简单想法就要先求a值，但是往往a值不好求，最后题解想了
个不求a值的方法求出了b值。
'''