'''
执行用时：44 ms, 在所有 Python3 提交中击败了70.86%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.99%的用户
通过测试用例：275 / 275

这题的解题速度有点慢了，算法不难就是模拟碰撞的过程，本以为15分钟写出来的。具体多久忘记了，
但调试循环，避免死循环就花了11分钟。技术还是差的远。

下面是官方题解代码：
class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans

看了官方代码结合我写的循环，得到些体会就是它借助for向右遍历，相当于我i += 1，因为每个条件都要考虑下标是否右
移，就很容易漏写。我觉得我一个循环的写法也没啥不好的，主要就是容易忘记更新变量，导致死循环。      我有一个理论，
当套用了很多程序语言的特殊语法后，就会简化代码编写。像这里它使用了while...else...，就写了一行append(new)
'''
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = [asteroids[0]]
        i = 1
        while i < (le := len(asteroids)):
            if asteroids[i] < 0:
                if not res or res[-1] < 0:
                    res.append(asteroids[i])
                else:
                    if res[-1] == -asteroids[i]:
                        res.pop()
                    elif res[-1] < -asteroids[i]:
                        res.pop()
                        i -= 1
            else:
                res.append(asteroids[i])
            i += 1

        return res