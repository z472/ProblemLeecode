class MyShitCodes:
    def lengthLongestPath(self, input: str) -> int:
        pass
# 作者：miaoch
# 不用递归子函数，逻辑大师
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        prefixSum = [0]
        res = 0
        for s in input.split('\n'):
            level = 0  # 当前层级
            while s[level] == '\t':
                level += 1
            sLen = len(s) - level
            # 如果是文件，比较最大值。
            if '.' in s:
                res = max(res, prefixSum[level] + sLen)
                continue
            # 如果是文件夹，将当前层级的字符串数目(包含末尾斜杆)保存。
            if level + 1 < len(prefixSum):
                prefixSum[level + 1] = prefixSum[level] + sLen + 1
            else:
                prefixSum.append(prefixSum[-1] + sLen + 1)
        return res

# 作者：miaoch

mt = ["dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
]
for i in mt:
    print(repr(i), Solution().lengthLongestPath(i))
'''
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
      "a",  "file1.txt\nfile2.txt\nlongfile.txt",
'''