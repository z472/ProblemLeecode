'''
一次过没啥好说的吧，这题
'''
class Solution:
    def lengthOfLastWord(self, s):
        # s: str) -> int:
        long, tag = 0, 0
        for i in range(len(s)-1, -1, -1):
            if tag == 0 and s[i] != ' ':
                tag = 1
                long += 1
            elif tag == 1 and s[i] != ' ':
                long += 1
            elif tag == 1 and s[i] == ' ':
                break
        return long

a = Solution()
mytest = ['hi s ', ' gjkf']
for i in mytest:
    print('in:|', i, '|')
    print(a.lengthOfLastWord(i))