'''
这题目一看就是回溯，但是实现难度还是比较大的。官方题解只提到了用状态压缩法表示集合状态，
具体代码实现的话，我对于状态压缩的重复性很疑惑，准确说就是当得到一个正确集合如何跳转状态。
看了下面网友的这个代码懂了，state中的每一位1表示已选择，n是当前集合的值，c是已凑好的集
合数量。这种写法就省略掉了每个集合的具体内容，向后的角度去看，这个内容对于判断是否能划分
是不必要的。  它算法简洁也是因为这点，只是保留必要的内容，它简化了代码。但是注意，仍然能
正确的回溯，这也是它正确性的前提。对于 [1,1,1,1,3,3,3,3] k=4这种用例是必须要回溯的。

这题官方说tc = O(n*(2^n)),n为Nums长度，[0,16]范围。但其实这是最差的复杂度。*-
'''
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:#如果不能平分为k个集合的话,直接返回False
            return False
        q = s // k  #每个集合的总和
        l = len(nums)
        def dfs(state, n, c):
            if state in cache:
                return cache[state]
            if c == k:
                cache[state] = True
                return True
            for i in range(l):
                if (state >> i) & 1 == 0:
                    res = dfs(state | 1 << i, n + nums[i], c) if n + nums[i] < q else dfs(state | 1 << i, 0, c + 1) if n + nums[i] == q else False #如果总和 + 插入的数字 大于单集合总和则不需要继续向下深搜
                    if res:
                        cache[state] = True
                        return True
            cache[state] = False
            return False
        cache = {}
        return dfs(0, 0, 0)
