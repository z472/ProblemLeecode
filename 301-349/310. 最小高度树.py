'''
我的提交->第一次bug解答错误，第二次超时错误。接着看题解。
看下题解的，虽然没有官方的但是网友的方法还是很赞。稍微分析一下，就是若一个结点 a 只与另一结点 b 有边。
a就一定不是根节点。可以假设它是，然后就会发现 a 的高度永远会比 b 高。反向思考，排除法不需要a。
    然后就是 删除 a-b 这条边。很大胆也很难理解的操作。不过确实并不影响寻找根节点。很难用逻辑来推导，
但可以说是一种 “尝试性”的操作。
    事实也证明了，删除是问题的本质。很多之前看不明朗的东西，在算法转编码过后，会发现看到了问题的本质。

我：不要再不思考就上什么“蛮力法”了。我太爱直接 蛮力法 遍历或是做什么了。
我下面的代码先是自己测试出了bug，力扣提交超时。不错的地方是 用集合来编码了。

知识收获：set()是可以用for 来遍历的。但顺序我不确定是否是加入顺序。
并集： set1 | set2     交集：  set1 & set2     取1中不包括2的： set1 - set2
集合可以 pop()    加入是 add()。  初始化1.set(iterable)  2.{i for i in range(3)}
'''
from typing import List
from collections import defaultdict

# 视图用限制遍历深度的，广度优先来遍历出结果。在1300个元素的时候就超时了。
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges:
            return edges

        d1 = defaultdict(set)
        for i in edges:
            d1[i[0]].add(i[1])
            d1[i[1]].add(i[0])

        def cd(mindeep: int, enter: int) -> bool:
            level1 = {enter}
            level0 = set()
            for _ in range(mindeep + 1):
                level2 = set()
                for j in level1:
                    level2 |= d1[j] - level0
                if not level2:      # bug
                    return True
                level0, level1 = level1, level2
            return False

        ret = []
        for i in range(1, n):
            for j in range(n):
                if cd(i, j):
                    ret.append(j)
            if ret:
                return ret


mt = [[4, [[1, 0], [1, 2], [1, 3]]],
      [2, [[0, 1]]],
      [6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]]]
ans = [[1], [0,1], [3,4]]
for i, j in zip(mt, ans):
    print(i, '\n\tright ans->', j, end='my ans')
    print(Solution().findMinHeightTrees(i[0], i[1]))
