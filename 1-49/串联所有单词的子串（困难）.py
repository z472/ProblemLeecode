class Solution:
    def findSubstring(self, s, words): # s为字符串，words是字符串列表，返回一个列表里面是符合题意的s的位置
        # words_indexs = [None for i in range(len(words))]
        a, b, c = len(s), len(words), len(words[0])
        occu = [None for i in range(b)]
        if a<b*c:
            return []
        froms = [None for _ in range(b)]
        for idx in range(a-b*c+1):
            for i in range(b):
                froms[i] = s[idx+i*c:idx+i*c+c]
            for idx, i in enumerate(froms):
                tag = words.count(i)
                if tag > 1:
                    occu[idx] = 





