'''
执行用时：216 ms, 在所有 Python3 提交中击败了66.34%的用户
内存消耗：25.4 MB, 在所有 Python3 提交中击败了68.40%的用户
看的官方题解，也很想动手用堆的结构来解题。算法构思部分，如果是在某个结构的特定位置保存着可供计算
的中位数，那么计算中位数操作就是O(1)的。还有就是维护一个 有序 的结构（因为中位数保存必是要有序）。
就联系到了两个优先队列，或是两个堆。一个最大堆，一个最小堆。然后就是平衡二者的数量。也不是很难。

编码时候遇到的问题。 超时，面对5万多次的操作。它会超时。原来是我向堆中 添加 某个值的时候。是先
用列表的append(i)然后heapq.heapfity(heap)。最好的是利用堆模块中的heapq.heappush(heap, item).

还有就是python 的 heapq 模块构造的是 最小堆。如何用它构造 最大堆。网上搜索一个是用 heapq 内部的函数，
貌似是不允许外界用的。函数的名前写了下划线。虽然能构造出 最大堆 。但是它的名字很繁琐且长。不是很方便。
第二个方法是取相反数放入最小堆中。很不错，我也是这么实现的。
'''
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftheapq = []
        self.rightheapq = []
        self.l1, self.l2 = 0, 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftheapq, -num)
        x = heapq.heappop(self.leftheapq)
        heapq.heappush(self.rightheapq, -x)
        self.l2 += 1
        if self.l2 > self.l1:
            y = heapq.heappop(self.rightheapq)
            heapq.heappush(self.leftheapq, -y)
            self.l2 -= 1
            self.l1 += 1

    def findMedian(self) -> float:
        if self.l1 > self.l2:
            return float(-self.leftheapq[0])
        return (-self.leftheapq[0]+self.rightheapq[0]) / 2

a = MedianFinder()
a.addNum(1)
a.addNum(4)
print(a.findMedian())
a.addNum(8)
print(a.findMedian())
a.addNum(3)
print(a.findMedian())
a.addNum(3)
print(a.findMedian())
a.addNum(3)
print(a.findMedian())


print(a.leftheapq)
print(a.rightheapq)
