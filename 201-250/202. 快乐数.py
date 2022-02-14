'''
执行用时：44 ms, 在所有 Python3 提交中击败了68.50%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了81.03%的用户
表现居然还可以。我这纯蛮力法。
官方：注意看题解里分析为何不会无限扩大的内容。很简单的思考，如果是也给三位数最大的999的平方和为243，别的位数也同理。
这里推理一下，就是一个n位数的最大情况平方和都比自己小，那么比他小的只能是要么在该位数下无限循环，要么是跳到更小的位数。
你虽然提交对了，但少了这个思考。

由于要存储一个记录曾经跑过值的数据结构，题解里用的set。故想能不能再减少sc呢。
由于结果要么是0要么是为一个循环。联想到之前141，142环形链表问题。可以用龟兔竞速的看能否在不为0的结点相遇即可。
def isHappy(self, n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        sav = []

        def calculate(x):
            ret = 0
            while x:
                ret += (x % 10) ** 2
                x //= 10
            return ret

        while n != 1:
            n = calculate(n)
            if n not in sav:
                sav.append(n)
            else:
                return False
        return True

mt = [19, 2]
for i in mt:
    print('in:', i, end='--')
    print(Solution().isHappy(i))

