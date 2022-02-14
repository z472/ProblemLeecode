'''
原创算法，小数据量证实正确，但是超时。题目如下：
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对 (h, k) 表示，其中 h 是这个人的身高，k 是应该排在这个人前面且身高大于或等于 h 的人数。 例如：[5,2] 表示前面应该有 2 个身高大于等于 5 的人，而 [5,0] 表示前面不应该存在身高大于等于 5 的人。
编写一个算法，根据每个人的身高 h 重建这个队列，使之满足每个整数对 (h, k) 中对人数 k 的要求。
示例：
输入：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出：[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''
class Solution:
    def recv(self, begin, end, k):
        min = -1    
        if not begin:
            begin.append([-1,0])
        for i in end:
            rk = 0
            if i[1]<=k:
                for j in begin:
                    if j[0]>=i[0]:
                        rk+=1
                if min==-1 and i[1]==rk:
                    min = i
                elif i[1]==rk and i[0]<min[0]:
                    min = i
        return min

    def reconstructQueue(self, people) :
        a = len(people)
        cbegin = []
        for i in range(a):
            h = self.recv(cbegin,people,i)
            cbegin.append(h)
            people.remove(h)
        cbegin.pop(0)
        return cbegin

s = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
right = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
a = Solution()
print(a.reconstructQueue(s) == right)
'''
解释：就对原列表操作，根据每个元素i中的i[1]，因为最终输出的第i个位置
（h,k）中k一定是小于等于该位置的位序i的，因为k是前面不矮于你的元素个数，
站在第3位（输出列表里为第二），它的k最多是2。每个循环在原列表中搜索这样
的元素，然后选择他们中“合理”（满足已经放入输出cbegin中元素），还要在
“合理”的元素中找元素身高最矮的（不用考虑重复身高，因为他们k会在前面
由于不合理而淘汰）。recv函数返回一个值加到输出列表最后面，移除原列表中
的该值。   第一次的时候要加个[-1,0]的值来满足第一次的循环，而不影响后面。
O(n^3)结果超时。
'''
