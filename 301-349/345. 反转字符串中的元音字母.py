'''
闹着玩式的简单题
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ret = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if ret[left] not in vowels:
                left += 1
            elif ret[right] not in vowels:
                right -= 1
            else:
                ret[left], ret[right] = ret[right], ret[left]
                left, right = left+1, right-1
        return ''.join(ret)

mt = ["hello", "leetcode"]
for i in mt:
    print(i, Solution().reverseVowels(i))
