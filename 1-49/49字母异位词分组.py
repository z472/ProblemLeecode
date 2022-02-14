'''
一次过，但自知速度慢，占用内存大。s = ''.join(sorted(list(i)))这行就是很懒的写法。
不过官方的排序方法和我没差多少，另一种思路是记录字符数量，占用会多一丢丢，运行快一丢丢
'''
class Solution:
    def groupAnagrams(self, strs):
        # strs: List[str]) -> List[List[str]]:
        d1 = {}
        mar = 0
        res = []
        for i in strs:
            s = ''.join(sorted(list(i)))
            if d1.get(s) is None:   # py3中False == 0 故 not None和not 0结果是一样的,这里写成is None就好了
                d1[s] = mar
                res.append([])
                res[mar].append(i)
                mar += 1
            else:
                res[d1.get(s)].append(i)
        return res

a = Solution()
mytest = [["eat", "tea", "tan", "ate", "nat", "bat"], ['eat', 'tea', 'ate']]
for i in mytest:
    print('hey:', i)
    print(a.groupAnagrams(i))
