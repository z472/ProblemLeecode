'''
执行用时：40 ms, 在所有 Python3 提交中击败了71.97%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了25.98%的用户
困难一次过，主要也是它的输入测试用例的n就只有1-9，比较少，自己都可以测试好再提交
    最大收获就是child(list1, kk % divider, divider//(len(list1)))这个
bug的修改因为之前有一个pop操作，所以它的长度是减少了一个，到这里的时候len(list1)
就是传入长度-1的值。
    官方题解：也是一个思路但是它是非递归实现的，很多人也是非递归。没懂它的order是
什么东西。其他有个valid是它说的用来保存是否用过这个数的列表。
    class Solution:
    def getPermutation(self, n, k):
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)
'''
class Solution:
    def getPermutation(self, n, k):
        # n: int, k: int) -> str:
        global restr
        restr = ''
        sav = [str(i) for i in range(1, n+1)]
        divider = 1
        for i in range(n - 1, 1, -1):
            divider *= i
        def child(list1, kk, divider):
            global restr
            if len(list1) == 1:
                restr += list1[0]
                print('before return ->', restr)
                return
            restr += list1.pop((kk-1)//divider)

            child(list1, kk % divider, divider//(len(list1)))

        child(sav, k, divider)
        return restr

a = Solution()
mytest = [(4, 9), (6, 3)]
for i in mytest:
    print('in:', i)
    print(a.getPermutation(i[0], i[1]))