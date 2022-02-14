'''
执行用时：44 ms, 在所有 Python3 提交中击败了50.49%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了10.58%的用户
    一次过，感觉递归还是蛮简洁的，循环分两个阶段，对于备选结果sav也只是在增加时有用append，弹出是用末尾的pop()。很大程度上类似于77,78
两题。但这里所给数组中的数可以重复会增加一定难度。把0个，1个，多个相同的数看成是一个整体，就好去理解了。
    速度：写的时候在递归传参那里纠结了一会，然后就是写的时候由于是光靠脑袋想，一段时间内是用了多个写法来写一段逻辑，就导致部分变量逻辑出错。
还是要在纸上厘清的方法更快速。 还有慢的一个点，就是各个if判断的边界值有点马，像我的枪法一样，好几天没写了，变的马了好多，在自己输入值测试的
时候的2-3个bug都是这个原因。还要多熟练。
'''
class Solution:
    def subsetsWithDup(self, nums):
        # nums: List[int]) -> List[List[int]]:
        res = [[], ]
        sav = []
        nums.sort()

        def child(sta):
            # 下个数字的位序i
            addn, tag = 0, 0
            if sta == len(nums):
                return
            while addn >= 0:
                if tag == 0:
                    sav.append(nums[sta])
                    res.append(sav[:])
                    addn += 1
                    if sta + addn == len(nums) or nums[sta + addn] != nums[sta]:
                        tag = sta + addn
                else:
                    child(tag)
                    if addn > 0:
                        sav.pop()
                    addn -= 1
            return

        child(0)
        # print(res)
        return res


a = Solution()
mt = [[1, 1, 2, 2], [1, 1, 2, 3, 3, 4, 4], []]
cou = 0
for i in mt[1:2]:
    print('in:', i)
    for j in a.subsetsWithDup(i):
        print(j, end='  ')
        cou = (cou + 1) % 6
        if cou % 6 == 0:
            print()
