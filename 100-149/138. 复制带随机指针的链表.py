'''
执行用时：48 ms, 在所有 Python3 提交中击败了52.75%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了15.37%的用户
最开心是一次过，自己测试也没有bug。 不过即使借用了133的存储结构和递归写法。可是我写的也是比较缓慢的。主要是两天没写了。
还有就是对象引用是否可以做字典的键等知识的缺乏，还有就是递归的逻辑差了些，边写边想。
官方题解：法一想象成一个图，法二就是走next和random，只要把没创建过的结点给赋值即可，法三：
https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-by-leetcod/
法三：O(1)空间复杂度的算法。分三步在上面的网址里。先遍历结点让新旧结点交叉在一起，然后修改新结点的random和next。画图的话还很好理解。
这也比法二的纯递归的过程要清晰，我那个自己都不确定递归到哪去了，也不确定是否正确，要靠测试的多种输入。
'''
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodeelapsed = {None: None}

        def cd(nodeori: Node) -> Node:
            if nodeori in nodeelapsed:
                return nodeelapsed[nodeori]

            res = Node(nodeori.val)
            nodeelapsed[nodeori] = res
            if nodeori.random == nodeori or not nodeori.random or nodeori.random in nodeelapsed:
                res.random = nodeelapsed[nodeori.random]
            else:
                res.random = cd(nodeori.random)
            res.next = cd(nodeori.next)
            return res

        return cd(head)

# print('__hash__' in dir(Node(3)))
def printNodecopy(node:Node):
    res = []
    while node.next:
        x = [node.val, node.next.val]
        if node.random:
            x.append(node.random.val)
        else:
            x.append(node.random)
        res.append(x)
        node = node.next
    res.append([node.val, None, node.random.val if node.random else node.random])
    return res

p1, p2, p3, p4 = Node(1), Node(2), Node(3), Node(4)
p1.next, p1.random = p2, p1     # random自己
p2.next, p2.random = p3, p1     # r前面
p3.next, p3.random = p4, None     # r后面
p4.next, p4.random = None, p1
for i in printNodecopy(Solution().copyRandomList(p1)):
    print(i)
