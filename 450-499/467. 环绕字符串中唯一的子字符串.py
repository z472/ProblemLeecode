'''
执行用时：64 ms, 在所有 Python3 提交中击败了95.24%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了6.88%的用户

在想到用 首字符+字符串长度的方式去用长的取代短的，局势就很明朗了，然后就是如何计算得到的
26个字符串，第一次想的算法不对，是贪心的不完全所致；第二次处理是完全的贪心出 首字符+最长
该字符的长度。
'''
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        def getlen(idx):
            start = idx
            idx += 1
            while idx < len(p) and (1 + ord(p[idx - 1]) - ord('a')) % 26 == ord(p[idx]) - ord('a'):
                idx += 1
            return idx - start

        dlongest = {chr(97 + i): -1 for i in range(26)}
        pi = 0
        while pi < len(p):
            curlen = getlen(pi)
            if dlongest[p[pi]] < curlen:
                dlongest[p[pi]] = curlen
            pi += curlen

        def showcurdict(time):
            print('\n',time,':')
            for i in dlongest.items():
                if i[1] > 0:
                    print(i)
        showcurdict(1)
        for si in dlongest:
            for idx in range(1, min(dlongest[si], 26)):
                firstchar = chr((ord(si)+idx-97)%26+97)
                if dlongest[firstchar] < dlongest[si]-idx:
                    dlongest[firstchar] = dlongest[si]-idx
        showcurdict(2)
        res = sum([_ for _ in dlongest.values() if _ > 0])
        return res



test = ['cac', 'zab', 'a']
wrong = ['zaba']
for i in test+wrong:
    print(i, ':', end='')
    print(Solution().findSubstringInWraproundString(i))