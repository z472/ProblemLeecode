"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
学到一点：
collections.deque.extend(iterable)
    把一个可迭代对象放入队列的右端
'''
# 这是官方的广度写法。存结点罢了。那个技巧可以哦。

def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root is None:
        return []
    result = []
    queue = collections.deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):     # 危险写法，我觉得不应该这么写。
            node = queue.popleft()
            level.append(node.val)
            queue.extend(node.children)
        result.append(level)
    return result
