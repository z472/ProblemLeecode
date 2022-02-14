'''
执行用时：44 ms, 在所有 Python3 提交中击败了29.85%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了8.84%的用户
一次过的简单题被打的满地找牙，离谱。感觉挺简洁啊。
官方题解：无。没啥意思。
'''
class Solution:
    def plusOne(self, digits):
        # digits: List[int]) -> List[int]:
        le = len(digits)
        for i in range(le-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        if digits[0] == 0:
            return [1] + digits

a = Solution()
mt = [[1,3], [9,9], [0], [8, 9, 9]]
for i in mt:
    print('in:', i)
    print(a.plusOne(i))
