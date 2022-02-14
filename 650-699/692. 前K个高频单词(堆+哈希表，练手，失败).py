'''
大致思路不难想，就是哈希表记录频率，然后堆来排序输出，令人疑惑的地方是
它说对于同样频率的值的比较是“字母顺序”，这应该是汉译的问题，这里我写不出来。
对于["i", "love", "leetcode", "i", "love", "coding"]这个用例
来说，当k为2输出为'i','love';当k为3输出居然就为 ， ，'coding'。它的字母顺序
难道是字母的字典序小的优先？那么写后，第105用例就是['a','aa','aaa']，k=1,答案输出
'aaa'。所以看下网友的题解：（他的注释不太懂，不过就学到一个重写比较函数，可以的）
class Word:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):  # True: self比other先淘汰
        if self.cnt > other.cnt:  # freq小的先弹出
            return False
        elif self.cnt < other.cnt:
            return True
        else:
            return self.word > other.word  # 字典序大的先弹出


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # time: nlogn
        # space: n
        q = []
        freq = collections.Counter(words)
        for word, cnt in freq.items():
            heapq.heappush(q, Word(word, cnt))
            if len(q) > k:
                heapq.heappop(q)
        res = []
        while q:
            res.append(heapq.heappop(q).word)  # 先弹出的是频率较小的，结果要逆序
        return res[::-1]

'''
import heapq
from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for i in words:
            d[i] += 1
        h = []
        rever = lambda s:''.join([chr(97+122-ord(_)) for _ in s])
        for item in d:
            heapq.heappush(h, (d[item], rever(item), item))
        return [_[2] for _ in heapq.nlargest(k,iterable=h)]

test = [(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
        (["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["i","love","leetcode","i","love","coding"], 3)]
for i in test:
    print(Solution().topKFrequent(i[0],i[1]))


