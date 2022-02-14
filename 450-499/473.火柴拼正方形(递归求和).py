'''
执行用时：224 ms, 在所有 Python3 提交中击败了70.60%的用户
内存消耗：22.6 MB, 在所有 Python3 提交中击败了5.18%的用户

我只想说过的艰难，成功的这份代码很短逻辑很秀很绕，复用度很高，第一天的代码把递归探查到
一条边的结果回退出来，然后想的是执行三次查到三条边即可。然而遇到一个致命的逻辑错误就是
当用例为：[3,3,3,3，4,4,4,4,5,5,5,5,]它的探查逻辑是升序后，用for遍历的去取值，当取
太多就导致gapint为负要返回错，查到gapint==0则为找到一条边。这里的致命错误就是得到正方
形的边长的组合是有多种的，而且是用上面的代码格式是无法解决的。因为我是在makesquare函数
内的子函数去执行查找边的逻辑，而上面的问题需要回退正确的边(该组合只是获得了部分正确的边)

修改：首先找到一条边然后是带着当前选取的火柴棍的位序去继续找一个边，显然这是可以连续写在
递归函数内的。让”正确“找到一条边不是回退出来，而是继续找下一个边。这样就实现了回退部分正
确的边的逻辑。哦对了，我还在这个过程中抛弃了昨天那个递归参数的写法，现在是用01表示占位与
否，也不去修改原来的数据。一切看上去都很完美。Second问题，用例：[1, 3, 3, 3, 3, 3,
6, 6, 7, 7, 7, 9, 10, 10, 10]会导致超时，这个用例的运行我没有debug去看，但应该就是
数据太长，且因为我的写法，每个组合是用位序来区分的不是具体的值来，相信该用例有太多组合可以
达到边长，就要频繁回退。抱着投机的心态装饰了一个lru缓存，这也是常见的递归写法，居然就过了。
'''
from functools import lru_cache

class Solution:
    def makesquare(self, matchsticks) -> bool:
        if sum(matchsticks) % 4:
            return False
        sidelength = sum(matchsticks) // 4
        matchsticks.sort()
        parseidxstr = lambda s: [idx for idx in range(len(s)) if s[idx] == '1']
        cache = []
        # 写个nb的递归，有下沉有回退
        @lru_cache(maxsize=None)
        def getoneside(idxstr, gapint):
            nonlocal cache
            if gapint < 0:
                return False
            elif gapint == 0:
                if idxstr.count('1') == 0:
                    return True
                print('gapint == 0:', idxstr)
                gapint = sidelength

            # idxstr 定长为 len(matchsticks)01字符串为了节约内存占用
            avaiable = parseidxstr(idxstr)
            for idx in avaiable:
                if getoneside(idxstr[:idx]+'0'+idxstr[idx+1:], gapint-matchsticks[idx]):
                    return True
            return False

        return getoneside('1'*len(matchsticks), sidelength)

test = [[1,1,2,2,2], [3,3,3,3,4]]
wrong = [[5,5,5,5,4,4,4,4,3,3,3,3],]
timeout = [[1, 3, 3, 3, 3, 3, 6, 6, 7, 7, 7, 9, 10, 10, 10],]
for i in wrong+timeout:
    print('i:', i, Solution().makesquare(i))
