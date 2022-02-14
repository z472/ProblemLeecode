'''
该题要求tc = O(N)。如果是正常的排序，然后把右边的值和左边的交叉出来就是对的。但它是O(NlogN)，
故它用了之前215中介绍的 快速排序的改写方法---快速选择。可以以O(N)复杂度寻找出无序中的第k位值，
题解里说的很好-“有序并不是我们需要的，我们只需要第k位的左值全部小于等于，右边都大于等于”。
    这个思想，相当于是用算法性能提高，同时丢弃了之前算法做多了的部分。   很极致化。

    如果是列表的话，就需要每个递归中去交换值。这里比较难写。    我是把几种情况改成了运算式来保存
    各种情况的信息。就是a,b = xxxx,xxxx那里。提升了很多代码的可读性。   我觉得写的前提是要多观察，
    然后把各种情况尽可能的压缩到一两条式子中，根据这个值来区分可以把很多本来用 单属性值（比如索引大小）
    之类的单属性根本会分到两条路径中，但操作是一种的情况的重复代码给合并到一个路径中。

    前提还是要对各种情况有个很好的理解。
'''
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # 快速排序方法找 nums 近似中位数
        lennums = len(nums)
        k = (lennums - 1) // 2
        print('k=', k)

        def changeklr(left, right) -> None:
            # 以left,right区间原本是在中间的值为分隔点左右修改，并按照哪个区间仍有外层要的索引值k
            nonlocal k
            trace = (left + right) // 2
            chl, chr = left, right
            while chl <= chr:
                a, b = (chl - trace) * (nums[chl] - nums[trace]), (chr - trace) * (nums[chr] - nums[trace])
                if a > 0 or (chl >= trace and a == 0):
                    chl += 1
                elif b > 0 or (chr >= trace and b == 0):  # 写成了 a==0
                    chr -= 1
                else:
                    nums[chl], nums[chr] = nums[chr], nums[chl]
                    if (chl - trace) * (chr - trace) > 0:
                        if chl > trace:  # 这里最初也有bug
                            nums[trace], nums[chl] = nums[chl], nums[trace]
                            trace = chl
                        else:
                            nums[trace], nums[chr] = nums[chr], nums[trace]
                            trace = chr
            if trace == k:
                return
            changeklr(trace + 1, right) if trace < k else changeklr(left, trace - 1)

        changeklr(0, lennums - 1)
        print('nums:', nums)
        nums[1::2], nums[2::2] = nums[k + 1:], nums[1:k + 1]
        print('exch:', nums)
        '''
        还没想好怎么交换得到最恰当的结果，nums[k]与前面或是后面的值相等就会出现交叉后的“错误”
        它比较可恶的是，快速选择不是排序出来的，nums[k]可能是 112 233 在右边，也可能是 1122 334
        在左边。当然右侧不是有序的，完全随机的。
        '''


mt = [[4, 1, 2, 6, 1, 2, 2], ]
bug = [[1, 2, 3, 2, 1, 3], [1, 4, 3, 4, 1, 2, 1, 3, 1, 3, 2, 3, 3]]
for i in mt + bug:
    print('\ninput', i)
    Solution().wiggleSort(i)

'''
写的交换函数主逻辑，还是存在部分错误的，不想改了。没有可读性，逻辑并不混乱但是肯定不好。
重复的代码也过，且没有一条逻辑的操作是覆盖多路径的。
            while chl < chr:
                if nums[chl] <= nums[trace] and chl <= trace:                    
                    chl += 1                    
                elif nums[chr] >= nums[trace] and chr >= trace:                    
                    chr -= 1
                elif nums[chr] >= nums[trace]:
                    nums[chr], nums[trace] = nums[trace], nums[chr]
                    trace = chr
                elif nums[chl] <= nums[trace]:
                    nums[chl], nums[trace] = nums[trace], nums[chl]
                    trace = chl
                else:    # 和trace等大的也放到右边
                    nums[chl], nums[chr] = nums[chr], nums[chl]
                    if chr <= trace:
                        nums[chr], nums[trace] = nums[trace], nums[chr]
                        trace = chr
                        chl += 1
                    elif chl >= trace:
                        nums[trace], nums[chl] = nums[chl], nums[trace]
                        trace = chl
                        chr -= 1
'''
