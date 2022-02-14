'''
执行用时：60 ms, 在所有 Python3 提交中击败了9.17%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了25.16%的用户
一次过，但是这表现，属实是拉跨啊。我还改进过它，减少递归的分支呢。
官方题解：深度遍历，广度遍历。下面有个网友的深度算法：和官方的深度基本一致，都是返回值包括都是使用一个哈希表（字典）来记录
是否到过这个结点。   他们俩都是很一致，但是由于代码写法（官方的我没复制）不同，他们运行差距还是不小的（下面是44ms，官方
比它要多8ms，sc也比官方要小）。
    评价：它这个代码很简洁，拥有不错的自明性。和官方的操作完全一致。
    分析总结：这种题是大的方向不多，但是具体自己去微操有很多不同，像我的方案看来虽然也是递归，但是具体的立意等细节和它的
不同，导致了代码复杂性等等的差距。甚至我针对题目输入中多个之间结点没有重复val的特性，对于一般的情况的 深度复制 会是错的。
所以现在的问题是怎么才能选出简洁的实现思路/编码方案？
    看了它的具体实现，发现我的破思路居然能正确做到，包括“优化”了两次，减少重复遍历，简直是个奇迹。
    一些看法：我思路的底子就和它的思路包括递归的操作和返回值都完全不同。我是在一个笨拙的底子上修改。
它是在一个好很多底子上修改。感觉像是电子产品那个一代的感觉。不好的版本，即使实现多么不易改了几次，但是
它的存在不会长久，会很快被好版本取代。像新技术取代旧的一样。      还是花功夫去优化方案的核心，直到新的
方案易于理解和实现或是不好继续优化为止。而不是在一个破的方案上去费力的修改。
    为何说了这么多一个中等题呢，这是第一道 图 的习题。而且是一个老现象了。同样的实现，但是具体操作不够
优秀，导致编码难度，速度，运行表现等等的差距。这是个现象。

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            #print(node.val)
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)
'''
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dpcopy = {node.val: Node(node.val)}
        elapsedval = []
        childelapse = []

        def cd(cur: Node):
            if cur.val not in elapsedval:
                for child in cur.neighbors:
                    if not dpcopy.get(child.val, None):
                        dpcopy[child.val] = Node(child.val)
                    dpcopy[cur.val].neighbors.append(dpcopy[child.val])
                elapsedval.append(cur.val)

            for child in cur.neighbors:
                if child.val > cur.val and child.val not in childelapse:
                    cd(child)
            childelapse.append(cur.val)

        cd(node)
        # print('CloneCode ', elapsedval, '\n\t', childelapse)
        return dpcopy[node.val]


p1, p2, p3, p4, p5, p6 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
p1.neighbors = [p2, p3, p4, p5]
p2.neighbors = [p1, p3]
p3.neighbors = [p1, p2, p4, p5, p6]
p4.neighbors = [p1, p3]
p5.neighbors = [p1, p3]
p6.neighbors = []


def printNode(p1):
    print(p1.val, ': [', end='')
    for child in p1.neighbors:
        print(child.val, end=',')
    print(']')
    for child in p1.neighbors:
        if child.val > p1.val:
            printNode(child)


printNode(Solution().cloneGraph(p6))


