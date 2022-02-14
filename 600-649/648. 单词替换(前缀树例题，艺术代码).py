'''
很明显最好的办法就是 前缀树，这种字符串判断的题，虽然不多但是最好的方法肯定就是它了。
不过要手动写的话就很不方便，来，学习下官方题解的代码。
'''
from functools import reduce
import collections
class Solution(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True  # True在py就是(int)1，False恒等于0

        for root in roots:
            # reduce第三个参数是可选的，置于迭代器最前面
            # 这个[END]是递归到最后dict的key，我觉得这是违规的吧，不过确实形象
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))

