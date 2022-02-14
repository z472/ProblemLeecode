'''
执行用时：64 ms, 在所有 Python3 提交中击败了5.49%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了93.75%的用户
通过测试用例：117 / 117

这题思考难度虽然不大，但是并不好写，可能是我太菜。虽然是一次过，但是编码速度还不够快。

下面是官方代码：
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

看官方写法后我感觉自己好脑残，这个循环写的。。。
'''
import string
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d1 = {i:None for i in string.ascii_lowercase}
        for i in range(len(s)):
            if not d1[s[i]]:
                d1[s[i]] = [i, i]
            else:
                d1[s[i]][1] = i
        res = []
        i,pre = 0,0
        while i < len(s):
            endindex = d1[s[i]][1]
            while i < endindex:
                endindex = max(d1[s[i]][1], endindex)
                i += 1
            i += 1
            res.append(i-pre)
            pre = i
        return res