class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True

mt = [4, 6, 30, 8, 9, 2, 5]
for i in mt:
    print(i, '\t', Solution().isUgly(i))

print(0%2, 0%3)