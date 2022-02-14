'''
执行用时：152 ms, 在所有 Python3 提交中击败了10.70%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了17.84%的用户
第一遍不写‘candidates = [i for i in candidates if i <= target]’还超时了，我丢？？？
下面复制了一个运行时间击败了98%用户的提交：
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(tar, idx, cur):
            if tar == 0:
                res.append(cur[:])
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                helper(tar - candidates[i], i + 1, cur)
                cur.pop()

        candidates.sort()
        helper(target, 0, [])
        return res
'''

class Solution:
    def combinationSum2(self, candidates, target):
        # candidates: List[int], target: int) -> List[List[int]]
        candidates.sort()
        candidates = [i for i in candidates if i <= target]
        if sum(candidates) < target:
            return []
        elif len(candidates) > 1:
            output = []
            for i in range(2):      # 先没有算首项，后算首项
                if target-candidates[0]*i == 0:
                    return [[candidates[0]]]
                child = self.combinationSum2(candidates[1:], (target-candidates[0]*i))
                if child:
                    for i_list in child:
                        add = [candidates[0]]*i + i_list
                        if add not in output:
                            output.append(add)   # [2]*0 -> [] ,[2]*1 -> [2]
            return output
        elif len(candidates) == 1:
            if candidates[0] == target:
                return [[candidates[0]]]
            else:
                return []
        else:
            return []
a = Solution()
mytest = [([2,3,6,7], 7), ([2,3,5], 7), ([2, 4, 5], 9), ([1, 1, 2, 5, 6, 7, 10], 8), ([1, 2, 2, 2, 5], 5), ([1,2,3,5], 6)]
outtime = [([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27
        ,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27)]
for i in outtime:
    print('candidate=:',i[0],' target=',i[1])
    print('output=',a.combinationSum2(i[0], i[1]))