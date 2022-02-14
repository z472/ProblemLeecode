'''
执行用时：32 ms, 在所有 Python3 提交中击败了94.12%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.06%的用户
一次过，主要利用了77题“组合”的方法，用个sav来保存动态的子集结果中的一个，不重复靠的是建立个
哈希表来记录nums值和它在nums中的位置，每个递归函数传递个参数k表示sav中要处理的位序k，它只
能用到d1[sav[k-1]]后面的nums中的值。而且比较好的设计就是每到一个子函数里，第一件事就是把
该位置的值加到sav里作为一个子集结果加到res中，就是向下延伸递归的过程中同时得到结果。结果为：
in: [1, 4, 7]
[[], [1], [1, 4], [1, 4, 7], [1, 7], [4], [4, 7], [7]]

官方题解：
'''
class Solution:
    def subsets(self, nums):
        # nums: List[int]) -> List[List[int]]:
        sav = [0] * len(nums)
        d1 = {i: idx for idx, i in enumerate(nums)}
        res = [[], ]
        if len(nums) == 1:
            return [nums, []]

        def child(k):
            for i in range(d1[sav[k - 1]] + 1, len(nums)):
                sav[k] = nums[i]
                res.append(sav[:k + 1])
                if k == len(nums) - 1:
                    return
                else:
                    child(k + 1)

        for j in range(0, len(nums)):
            res.append([nums[j]])
            sav[0] = nums[j]
            child(1)
        return res


a = Solution()
mt = ([1, 4, 7], [2])
for i in mt:
    print('in:', i)
    print(a.subsets(i))
