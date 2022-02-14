'''
官方题解和我想的方式差不多，只是实现有小的不同，替换一个字符的比较，确实只有
按位去存前一部分和后一部分，然后相对应比较即可。它的代码实现就是函数式编程大师（什么鬼东西）。
'''
import collections

class MagicDictionary(object):
    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))

    def search(self, word):
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._genneighbors(word))

