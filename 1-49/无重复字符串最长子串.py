'''
题目：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    如：‘bbb'，长度为1. 'fwwkew',长度为3（'wke'), 'abcabcbb'，长度为3（'abc','bca','cab')
解法1：蛮力法遍历，一次移动一个字符位置，算以它为起点最大的长度，然后赋值给max(这个名字还撞上了内置的函数名)
'''
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max = 0
#         if not s:
#             return 0
#         if len(s) == 1:
#             return 1
#         for j in range(len(s)):
#             now = 0
#             a = s[j:]
#             if max < len(a):
#                 for idx,i in enumerate(a):
#                     if i in a[:idx]:
#                         break
#                     else:
#                         now+=1
#                 if now > max:
#                     max = now
#         return max
'''
解法2.官方题解里的“移动窗口”法，大意就是设置两个左右指针，左指针不动，右指针向又移动，遇到一个重复字符就调整左指针的位置。
        这样的好处是：对比我那个一次移动一个位置来算最大长度的方法，它的左指针一次移动多个位置才计算一次长度。避免了不必要的
        “重复计算”。分析依据是：如果i起点的最大到右指针为ik,那么i到ik之间为起点的最大长度都要有一部分是包含到ik这段的。这段
        就是我重复计算的内容。
'''


def lengthOfLongestSubstring(s):
    # 左右指针，还有他们的移动的控制。建个set来判断重复
    left = 0
    s1 = set()
    maxx = 0
    for idx, i in enumerate(s):
        right = idx
        if i not in s1:
            s1.add(i)
        else:
            left += s[left:right].index(i) + 1   # bug:这里的.index返回值它的参照对象是切下来那段，不是原来那段
            s1 = set(s[left:right])
            s1.add(i)
        if len(s1) > maxx:
            maxx = len(s1)
    return maxx


print(lengthOfLongestSubstring("loddktdji"))
print(lengthOfLongestSubstring("aaaa"))
print(lengthOfLongestSubstring("fvfd"))
