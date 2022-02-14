'''
tc=124ms > 38%, sc > 99.2%
错了四次，但是完全自己写出的感觉实在是美妙。
下面是tc = 24ms。超过99%提交。也是官方题解里的数学方法，涉及到一个 贝祖定律，很复杂的感觉。

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
'''


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        z = [0, jug1Capacity, jug2Capacity, jug1Capacity + jug2Capacity]
        a = min(jug1Capacity, jug2Capacity)
        b = max(jug1Capacity, jug2Capacity)
        x = b
        if targetCapacity > a + b:
            return False
        while x != a:
            if targetCapacity in (x + a, x):  # x+a有一部分是>a+b的，但是被预处理了
                return True
            if x < a:
                if targetCapacity == x + b:
                    return True
                x = b - (a - x)
            else:
                x = x - a
            # print(x, end=' ')
        return targetCapacity in z


mt = [(2, 6, 5), (3, 5, 4)]
bug = [(1, 2, 3), (2, 4, 2), (34, 5, 31), (6, 9, 1), (4, 6, 8)]
for i in mt + bug:
    print(i, Solution().canMeasureWater(i[0], i[1], i[2]))
