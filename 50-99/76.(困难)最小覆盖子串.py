'''
执行用时：196 ms, 在所有 Python3 提交中击败了24.99%的用户
内存消耗：15.3 Ms, 在所有 Python3 提交中击败了5.04%的用户
我这个的写法就是官方题解的做法，双指针滑动窗口，用两个哈希表存储s,t的数据个数，然后用distance来表示窗口中
满足的t的个数来快速的判断ds窗口是否包含了全部的dt中的元素。要注意distance的维护，何时才能增加，何时才能减
少，还有l,r窗口两端的移动和ds内值的维护。   我只想那它来练习编码，但是发现卡了很久，在于循环和l,r值的维护上
'''
class Solution:
    def minWindow(self, s, t):
        # s: str, t: str) -> str:
        # 你能设计一个在 o(n) 时间内解决此问题的算法吗
        # if...else..如果if后面是多个条件，else很容易就会出错，建议只写单个条件。
        ds = {}
        dt = {i:t.count(i) for i in t}
        distance = 0
        l, r = -1, -1
        outl, outr = 0, len(s)
        # ds[s[0]] = 1
        while True:
            if distance < len(t):
                r += 1
                if r < len(s) and dt.get(s[r]):
                    ds[s[r]] = ds.get(s[r], 0) + 1
                    if dt[s[r]] >= ds[s[r]]:
                        distance += 1
                elif r == len(s):
                    break
            else:
                l += 1
                if l < len(s) and dt.get(s[l]):
                    ds[s[l]] -= 1
                    if dt[s[l]] > ds[s[l]]:
                        distance -= 1
                        if r-l < outr-outl:
                            outl, outr = l, r
                elif l == len(s):
                    break

        # print('distance, outl, outr, len(t), l, r, len(s)')
        # print(distance, outl, outr, len(t), l, r, len(s))
        # print(ds, '\n', dt)
        return s[outl:outr+1] if outr != len(s) else ''

a = Solution()
mt = [("ADOACBECODEBANC", 'ABC'), ('aa', 'a')]
for i in mt[:]:
    print('in:', i)
    print(a.minWindow(i[0], i[1]))