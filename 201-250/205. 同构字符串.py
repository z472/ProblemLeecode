'''
执行用时：44 ms, 在所有 Python3 提交中击败了88.66%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了41.53%的用户
官方题解也没啥好方法。水题，绝对是凑个数来的。
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapdict = {}
        savvalues = []
        for i in range(len(s)):
            if not mapdict.get(s[i]) and t[i] not in savvalues:
                mapdict[s[i]] = t[i]
                savvalues.append(t[i])
            elif mapdict.get(s[i]) and mapdict[s[i]] == t[i]:
                continue
            else:
                return False

        return True

mt = [('egg', 'add'), ('pa', 'ww')]
for i in mt:
    print(Solution().isIsomorphic(i[1], i[0]))