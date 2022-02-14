'''
我是伞兵，dp存起来然后减就完了。我是伞兵啊。
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        ret = 0
        for i in range(left, right+1):
            ret += self.nums[i]
        return ret