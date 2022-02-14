'''
执行用时：128 ms, 在所有 Python3 提交中击败了70.87%的用户
内存消耗：27.7 MB, 在所有 Python3 提交中击败了66.80%的用户
这道题看DataStructures目录下的Trie.py代码。模仿了一部分。
最大的收获是让我了解到某一种数据结构的拓展不必是要加入它自己，可以是整个类的对象作为该结构。想的太死板。
还有就是要注意字符串的收尾。
'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item = {'tag':0}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.item
        for i in word:
            if not p.get(i):
                p[i] = {'tag':0}
            p = p[i]
        p['tag'] = 1


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.item
        for i in word:
            if not p.get(i):
                return False
            p = p[i]
        return True if p['tag'] else False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.item
        for i in prefix:
            if p.get(i):
                p = p[i]
            else:
                return False
        return True

    # def showTrie(self, obj:Trie):
    #     pass

obj = Trie()
obj.insert('water')
print(obj.startsWith('wat'))
obj.insert(('wat'))
print(obj.search('wat'))