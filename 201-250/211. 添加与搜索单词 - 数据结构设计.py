'''
执行用时：128 ms, 在所有 Python3 提交中击败了94.41%的用户
内存消耗：23.3 MB, 在所有 Python3 提交中击败了99.34%的用户
先看的题解，py3他们说用长度字典来存单词，然后比较会快于 字典树。有点投机取巧了。收获就是用了filter，zip两个函数。
没有官方题解。
'''
from collections import defaultdict


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        self.word = word
        filterlist = list(filter(self.paircompare, self.dict[len(word)]))
        return True if filterlist else False

    def paircompare(self, dictword):
        for i, j in zip(self.word, dictword):
            if i != '.' and i != j:
                return False
        return True

obj = WordDictionary()
obj.addWord('word')
param_2 = obj.search('w..d')
obj.addWord('wd')
x = obj.search('w.')
print(param_2, x)