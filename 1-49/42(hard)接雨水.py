'''
    我这应该是用known来代表栈，从左到右一次遍历，根据栈顶元素去做不同操作，在编码的时候太离谱了，
各种低级失误。然后比较好的官方解法（官方给了4个）是双指针，一次遍历，靠着两端指针相互呼应的判断
来替代了栈保存数据的功能。仅仅需要一个if语句。
    关键不是怎么解单独的这道题，而是学习从和你相似的分析过程转化成不同于你代码的切入角度。
'''
class Solution:
    def trap(self, height):
        # (height: List[int]) -> int
        known = [(0,0,0)]   # (a,b,c) a-b 高度范围，c横坐标
        vol = 0
        for i in range(len(height)):
            if height[i] != 0:
                while known:
                    if height[i] > known[-1][1]:
                        addvol = (i-known[-1][2]-1)*(known[-1][1]-known[-1][0])
                        vol += addvol
                        known.pop()
                        if not known:
                            known.append((0, height[i], i))
                            break
                    else:
                        addvol = (i-known[-1][2]-1)*(height[i]-known[-1][0])
                        vol += addvol
                        if known[-1][1] == height[i]:
                            known.pop()
                        else:
                            known[-1] = (height[i], known[-1][1], known[-1][2])
                        known.append((0, height[i], i))
                        break
        return vol

a = Solution()
cla_test = [[0,2,0,2], [0,1,0,3],[0,3,0,1,2]]
lee_test = [[1,0,2,1,0,1,3,2,1,2,1], [4,2,0,3,2,5]]
for i in lee_test:
    print('height= ', i)
    print('vol=', a.trap(i))