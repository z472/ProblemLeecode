'''
执行用时：48 ms, 在所有 Python3 提交中击败了11.99%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了28.40%的用户
一个面向过程（流程固定且简单）的题。重点在练习编码。一个问题是自己的bug，循环出来的p1,p2值应该再
精确控制好。这次是多了一位。第二个点是在完成整个流程中同时最少的操作步骤，来提高速度。
下面的代码是 32ms,比我快了33%，击败95%的提交. 它的zip方法的利用我是第一次见到可以应用的这么舒适。
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        max_len = max(len(version1), len(version2))
        version1 = version1 + ['0'] * (max_len-len(version1))
        version2 = version2 + ['0'] * (max_len-len(version2))
        version1 = [int(i) for i in version1]
        version2 = [int(i) for i in version2]

        for v1, v2 in zip(version1, version2):
            if v1 == v2:
                continue
            elif v1 > v2:
                return 1
            else:
                return -1
        return 0
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revise1, revise2 = version1.split('.'), version2.split('.')
        p1, p2 = 0, 0
        lenrevise1, lenrevise2 = len(revise1), len(revise2)
        while p1 < lenrevise1 and p2 < lenrevise2:
            int1, int2 = int(revise1[p1]), int(revise2[p2])
            if int1 == int2:
                p1, p2 = p1 + 1, p2 + 1
                continue
            else:
                return 1 if int1 > int2 else (-1 if int1 < int2 else 0)

        remain1 = list(filter((lambda x:int(x)>0), revise1[p1:]))   # bug revise1[p1+1:]
        remain2 = list(filter((lambda x:int(x)>0), revise2[p2:]))   # bug
        print(remain1, remain2)
        return 1 if remain1 else (-1 if remain2 else 0)

mt = [('1.01','1.001'), ('1.0.0','1.0'), ('1.0.1','1'), ('7.5.2.4','7.5.3')]
bug = [('1','1.1')]
for i in mt+bug:
    print('in:', i, end='->')
    print(Solution().compareVersion(i[0], i[1]))
    print()