'''
    核心代码写的比你好看一些，它是交换来把首项给到后面的,利用输入数组的空间，减少空间占用。（我也是一次过的）
关于嵌套函数使用参数的问题，博客园自己写了篇博文。
class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res
'''


class Solution:
    def permute(self, nums):
        # nums: List[int]) -> List[List[int]]
        res = []
        if len(nums) > 1:
            for i in nums:
                x = [ch for ch in nums if ch != i]
                for j in self.permute(x):
                    res.append([i] + j)
            return res
        elif len(nums) == 1:
            return [nums]
        else:
            return []


a = Solution()
mytest = [[1, 2, 3], [0, 3, 4, 2], [], [2]]
for i in mytest:
    print('输入:', i)
    print('输出:', a.permute(i))
