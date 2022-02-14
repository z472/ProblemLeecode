'''
这题我以为是两个二叉搜索树呢，一个代表重复两次的时间区间，一个是当前覆盖的时间区间，先后去两个里面搜索，更新。

然后官方题解的代码，直接列表，无语...

class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True

tc = O(n^2)
'''