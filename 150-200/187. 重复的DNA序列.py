'''
https://blog.csdn.net/lucylove3943/article/details/83491416
上面介绍的是Rabin-Karp算法。
    一种字符串搜索（查重）算法。把一段字符串用数字代替，然后计算出一个哈希值，通过比较哈希值来比较
两个字符串是否相同。计算式在网页里有，它又加入滑动窗口的感觉。让计算下一个哈希值时仅需O(1)的操作来修改
之前的值。O(m+n)

法二：二进制掩码，思路类似RK算法。但是不用哈希值，而用一个二进制位串来代替哈希值保存在hashset里。
看不懂算法细节。但总体也是和RK一样。只有第一个用计算一个完整的位串，后面每个都在前一个基础上修改。

看了网友的题解，也大都不用二进制掩码。还是用蛮力的多。
'''
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lens = len(s)
        pass