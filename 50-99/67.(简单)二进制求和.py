'''
执行用时：64 ms, 在所有 Python3 提交中击败了6.38%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了24.45%的用户
一次过，但是写的代码极其丑陋，我实在觉得不是很好写这东西。
官方题解：
1.不健壮版本：
class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
补充知识：{index(指定选择后面第几个参数):后面一顿修饰符}.form-
-at(多个字符串参数，也可以是列表，字典（相应处理不同）)
仅限于py和java本身有高精度的功能，Java还是有位数限制。不过也是
非常简洁的py3思路。
2.模拟--竖式相加：
和你一样，进位然后相加。
3.利用位运算实现，末位相加，进位等操作。但它的算法细节和模拟区别很大很大：
把 a 和 b 转换成整型数字 x 和 y，在接下来的过程中，x 保存结果，y 保存进位
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y          # 异或运算，计算无进位运算的结果
            carry = (x & y) << 1    # 与运算，计算全位置的进位并左移
            x, y = answer, carry
        return bin(x)[2:]
解释：https://leetcode-cn.com/problems/add-binary/solution/er-jin-zhi-qiu-he-by-leetcode-solution/
第一次循环是计算最后一位，然后与左移把进位给到上面，这个过程重复去做，后面循环就是前两个值的进位与前两个值的无进位结果加和
左移操作后位补零，保存了之前后几位的正确结果因为(与0运算)是不变的原数的。这就是我对它全部的理解了，还有很多问题。
'''
class Solution:
    def addBinary(self, a1, b1):
        # a: str, b: str) -> str:
        la, lb = len(a1), len(b1)
        a, b = [int(i) for i in a1], [int(j) for j in b1]
        ma, mi = max(la, lb), min(la, lb)
        res, add = [0]*ma, 0
        for i in range(ma-1, -1, -1):
            if ma-mi <= i <= ma-1:
                res[i], add = str((add+a[i-ma]+b[i-ma])%2), (add+a[i-ma]+b[i-ma])//2
            elif la > lb:
                res[i], add = str((a[i]+add)%2), (a[i]+add)//2
            else:
                res[i], add = str((b[i]+add)%2), (b[i]+add)//2
        return '1'+''.join(res) if add == 1 else ''.join(res)

a = Solution()
mt = [('101', '0'), ('111', '11'), ('1011','1101')]
for i in mt[:]:
    print('in:', i[0], '+', i[1], '=', a.addBinary(i[0], i[1]))