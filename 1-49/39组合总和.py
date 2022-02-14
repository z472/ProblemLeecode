'''
正确，但是官方题解里说还有“剪枝”的写法，就是优化它的写法。还可以挖掘一下
'''
class Solution:
    def combinationSum(self, candidates, target):
    # candidates: List[int], target: int , return -> List[List[int]]
        if len(candidates) > 1:
            first, output = 0, []
            while first < target:
                child = self.combinationSum(candidates[1:], (target-first))
                if child:
                    for i_list in child:
                        output.append([candidates[0] for _ in range(first//candidates[0])] + i_list)
                first += candidates[0]
            if first == target:
                output.append([candidates[0] for _ in range(first//candidates[0])])
            return output
        elif len(candidates) == 1:
            if target % candidates[0] == 0:
                return [[candidates[0] for _ in range(target//candidates[0])]]
            else:
                return []
        else:
            return []

a = Solution()
mytest = [([2,3,6,7], 7), ([2, 5], 9), ([2, 4, 5], 12), ([4,3], 10), ([], 0), ([2, 7], 1)]
for i in mytest:
    print('candidate=:',i[0],' target=',i[1])
    print('output=',a.combinationSum(i[0], i[1]))