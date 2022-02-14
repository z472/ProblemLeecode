'''
执行用时：40 ms, 在所有 Python3 提交中击败了59.64%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.28%的用户
一次过，也几乎没出现bug，有个地方忘记改了，就一个小地方。但是
我最初的想法是双向进行的，我也是想到左边的一部分镜像的写右侧的
部分，但是我脑子被两边的执行细节缠住了，后来又想了很多很久的执
行细节，发现既然是镜像的，不如先写一侧的代码，写透彻些。然后就
又发现可以写出正确的执行，变量都很清楚。最初我是想找到左边的1
和右边的1构成一个门，然后遍历门内值，0就去左边门交换，2就去右
边，但是又出现了如如果一侧有1另一侧没1，还有门内值与1交换之后
1的新标记位置是什么，都和我下面的代码问题相似，但是少了一侧的
约束，在左边为2右边为2时是要遍历右侧，直到左移找到了一个比2小
的就后续操作，这里。让我觉得好像无法完全镜像的写双向遍历，因为
这里左右的情况是一样的，应该让一边去遍历。

官方题解：本题是经典的荷兰国旗问题。
法一：单指针，走两遍，第一次把0放到最左边，第二次把2放到最右边
法二：双指针版本1
具体地，我们用指针p0来交换 0,p1来交换 1，初始值都为 0。从左向右遍历，遇到0
与p0交换，遇到1与p1交换，然后都要把p0,p1加一。此时p0和p1都是代指0和1的末尾
位置的后一位，这就会遇到一个情况，p0和后面的pi交换导致把1给交换掉了。也就是p0
<p1时会出问题，需要再把pi和p1交换，因为p0与pi交换把pi变成1了。循环仍能正常运作。
    双指针版本2
p0从左边遍历来标记0，p2从右边遍历来标记2。和上个版本一样的交换然后p0+1，p2-1。
如果p0==p2则结束。当我们找到2时，我们需要不断地将其与进行交换，直到新的pi不为2，
而这里也会遇到一种情况就是pi，p2同时为2,如果交换pi+1就出错了，和我遇到同样的问题。
只需要p2-1找到不为2的值即可。
下面是版本1代码：
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
看了官方的几个版本的解法，双指针的是符合要求的一次遍历，而且它用p0p1来标记了0和1的最后一位的后一位，
交换+1，然后就是维护循环的正确性了。我和它双指针版本2的区别在于我没有标记0的操作，我只有标记1的最左
端的操作，右边ri也是2的左端。学习下它这种”先确定核心思想操作--在去维护异常情况“的写法。我算是面向全
过程编写的，没有固定的变更操作，很多特例化情况都写一遍。
'''
class Solution:
    def sortColors(self, nums):
        """
        nums: List[int]) -> None:
        Do not return anything, modify nums in-place instead.
        你可以不使用代码库中的排序函数来解决这道题吗？
        你能想出一个仅使用常数空间的一趟扫描算法吗？
        """
        le = len(nums)
        li, ri = 0, le-1
        l1 = le
        while li <= ri:
            if nums[li] == 2:
                if nums[ri] == 0:
                    # 交换ri,li
                    if l1 > li:
                        nums[li], nums[ri] = nums[ri], nums[li]
                    else:
                        nums[li], nums[l1], nums[ri] = nums[l1], nums[ri], nums[li]
                        l1 += 1
                elif nums[ri] == 1:
                    # 交换ri,li,左1为li
                    nums[ri], nums[li] = nums[li], nums[ri]
                    if l1 > li:
                        l1 = li
                else:
                    # ri左移直到不为2然后就走前两个if
                    ri -= 1
                    continue
            elif nums[li] == 1:
                if l1 > li:
                    l1 = li
            else:   # 左边遍历的值为0时，若为左1的左侧不动它
                if l1 < li:     # 遍历到左1的右侧
                    nums[li], nums[l1] = nums[l1], nums[li]
                    l1 += 1
            li += 1
        print(nums)

a = Solution()
strs = ['10200211', '212120', '202110', '201', '0', '1']
for j in strs[1:]:
    mt = ([int(_) for _ in j],)
    for i in mt:
        print('in:', i)
        a.sortColors(i)