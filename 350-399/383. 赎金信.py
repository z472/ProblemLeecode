from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(magazine)
        for i in ransomNote:
            if c1.get(i):
                c1[i] -= 1
                if c1[i] == 0:
                    del c1[i]
            else:
                return False
        return True

mt = [('aa', 'aab'), ('aa', 'ab'), ('c', 'bn')]
for i in mt:
    print(i, '->', Solution().canConstruct(i[0], i[1]))
