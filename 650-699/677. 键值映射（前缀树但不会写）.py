'''
我写的前缀树比这个官方题解的要简洁，它是之前648题代码的样子，没有运行报错，但是返回值为0，
没搞懂哪里有bug，那份被我删掉了。下面这个官方题解代码就很直白了，像我平时写的风格，ONO

这个题知道用前缀树后，其实伪算法就很明晰了，但是又可以有实现的差异，也可以不在每个结点都保存值。
因为前缀树最后的结点空间一般都有标记嘛，就可以只设置标记为val，然后每次sum, 就dfs去计算即可。
下面这个方案也可以。
'''
class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.root
        for c in key:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = TrieNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.next[ord(c) - ord('a')] is None:
                return 0
            node = node.next[ord(c) - ord('a')]
        return node.val

