'''
闹着玩似的简单题
'''
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lens = len(s)
        for i in range(lens//2):
            s[i], s[lens-1-i] = s[lens-1-i], s[i]
        print(s)

mt = ['abcde', 'abdc']
for i in mt:
    print(i, end=' ')
    Solution().reverseString(list(i))


