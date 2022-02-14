'''
执行用时：44 ms, 在所有 Python3 提交中击败了6.69%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了88.96%的用户
通过测试用例：308 / 308

虽然是双层循环，但是内循环只会执行一次。感觉py的int()方法，可以把前置零的数字字符串正确转化为Int数。
方便了很多。比如 110，这种输入。

这题没难度，纯练手。
'''
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 275 154 110
        res = str(n)
        for i in range(1, len(res)):
            if res[i] < res[i-1]:
                for j in range(i-1, -1, -1):
                    if res[j] < res[j+1]:
                        res = res[:j + 1] + str(int(res[j + 1]) - 1) + '9' * (len(res) - j - 2)
                        break
                else:
                    res = res[:j] + str(int(res[j]) - 1) + '9' * (len(res) - j - 1)
                break
        return int(res)

test = [110, 275, 3325]
for i in test:
    print(f'i={i}->',Solution().monotoneIncreasingDigits(i))