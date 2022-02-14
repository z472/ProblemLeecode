'''
第33题的延伸，这回数组中可能包含重复元素
执行用时：32 ms, 在所有 Python3 提交中击败了96.61%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了17.58%的用户
第三次过的，第一次是没考虑到初态为[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]的输入。第二次是个条件判断细节没写对。感觉
这题还有一种写法用nums[l] >= nums[r]作为核心判断的，它其实是表示翻越过最高点之后的情况，那时候就是完全的升序二分法即可。
这道题比较好的一点是在之前33的基础上加了一种l,mid,r都相等的情况，这时候两边都不确定该怎么走，就是要递归着都去看一看。之前那个
题可以说是二分法的改良，初末两种状态感觉并不是非常有影响，但是这题就像80题一样，过程中会产生一种状态，需要去处理，之前的话是为
初态写的路径然后末态也可以正常走。   这题我在第一次错之后，开始怀疑是不是很多条件因为相等这个变化导致出问题，脑补了相等对初态的
种种影响，但是没脑补出来，就只针对l=mid=r的情况去改了，额，有点运气成分，即使是通过后我对路径还是有点懵的，就靠输出的l,r的正确
与否来判断路径是否走对了，其实也就是跨越max点之前是很关键的，后面都是正常二分法了，但之前状态的代码是否对正常二分有副作用也没看。
还是有点迷糊，感觉用nums[m]和nums[l]为核心的路径不是很简明，最初是因为nums[l]>=nums[r]而且是怎么走要看mid嘛就这么写的，没
有针对两种状态。

官方题解：
'''


class Solution:
    def search(self, nums, target):
        # nums: List[int], target: int) -> bool:
        l, m, r = 0, 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                print('1', end='')
                print('l, r=', l, r)
                return True
            if nums[m] < nums[l]:  # 初态：nums[l] > nums[m]
                if target > nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
            elif nums[m] > nums[l]:  # 初态：mid > nums[l] >= nums[r]
                if target < nums[m]:
                    if target <= nums[r]:
                        if nums[r] <= nums[l]:  # 初态,第二次错在这里没写等号，走错路了
                            l = m + 1
                        else:  # 末态
                            r = m - 1
                    else:
                        r = m - 1
                else:  # target >= mid
                    l = m + 1
            else:  # 初态：nums[m] == nums[l] >= nums[r]
                if nums[l] > nums[r]:  # 这里因为是target不等于nums[m]，故如果mid==nums[l]
                    l = m + 1
                else:
                    return self.search(nums[l:m], target) or self.search(nums[m + 1:r + 1], target)
        print('l, r=', l, r)
        if r < 0 or l > len(nums) - 1:  # 递归出循环可能越界了也没找到，越界应该是切片给的第一个列表为空，让r为-1了
            return False
        if target == nums[r]:  # 下去整，r<l，不取等会考虑不到最后一个
            print('2', end='')
            return True
        return False


a = Solution()
mt = [([3, 5, 6, 0, 0, 1, 2], (-1, 0, 2, 3, 7, 1, 5)), ([1, 5], [])]
for i in mt[0][1]:
    print('target:', i, a.search(mt[0][0], i))
# print(len([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]))
# print(a.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 0))  # target = 0, 2, 3
# print(a.search([1,2,2,2,0,1,1], 0))
