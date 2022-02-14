'''
存每个位置左边的连续1的长度，这样就转化成了和84柱状图一样的（竖着看一样）题目，每次遍历一列，做上述操作，时间复杂度为O(mn).
把写的任务留给。。。
'''
class Solution:
    def maximalRectangle(self, matrix):
        # matrix: List[List[str]]) -> int:
        