'''
执行用时：36 ms, 在所有 Python3 提交中击败了80.24%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.16%的用户
一次过，但是感觉难度主要在于你对变量的修改上，对判断条件的辨别
中，浪费了很多时间。

代码：很丑陋，变量如果不写注释根本不好理解，对于边界值的操作不
好脑补，很大程度是依靠测试结果来更正的，在补空格那里你占用空间
可能多了点。

官方题解：无。看了几个Py3题解都写了挺多的，看来并无好的思想，
感觉就是练习细心的题。
'''
class Solution:
    def fullJustify(self, words, maxWidth):
        # words: List[str], maxWidth: int) -> List[str]:
        res = []
        addle, i_sta, i_end, savline, idx = 0, 0, 0, '', 0
        while idx < len(words):
            le = len(words[idx])
            if addle == 0:
                i_sta = idx
            if addle + le + 1 < maxWidth:
                addle += le+1
            else:
                if addle + le > maxWidth:
                    i_end = idx-1
                    idx = idx-1
                    addle -= 1
                elif addle + le == maxWidth:
                    i_end = idx
                    addle += le
                else:
                    addle += le
                    i_end = idx
                for j in range(i_sta, i_end):
                    if j - i_sta + 1 <= (maxWidth-addle) % (i_end-i_sta):
                        savline += words[j]+' '*((maxWidth-addle)//(i_end-i_sta)+2)
                    else:
                        savline += words[j]+' '*((maxWidth-addle)//(i_end-i_sta)+1)
                savline += words[i_end]
                res.append(savline+' '*(maxWidth-len(savline)))
                savline = ''
                addle = 0
            idx += 1
        if addle != 0:
            str = ' '.join([i for i in words[i_end+1:]])
            res.append(str+' '*(maxWidth-len(str)))
        return res

a = Solution()
mt = [(["This", "is", "an", "example", "of", "text", "justification.", 'kk'], 16), (['asd', 's', 'sdf', 'd', ], 7),
      (["What","must","be","acknowledgment","shall","be"], 16), (["Science","is","what","we","understand","well",
    "enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)]
for i in mt[:]:
    print('in:', i[0], i[1])
    for j in a.fullJustify(i[0], i[1]):
        print(j, len(j))