'''
执行用时：40 ms, 在所有 Python3 提交中击败了81.08%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了14.29%的用户
一次过，算法的第一个版本在最下面，是审题出现了问题，这个版本的算法最初看了下官方题解的方法，知道是递归去求解，也就相当于是
纯粹的练习编码了。官方题解就一个思路。还是比较有局限的一个题。主要说下，子函数的x变量，它是为了判断后续长度而生的，是当前要
插入sav列表的最起码的长度（长度范围是1-3），它的上限其实也可以求出，但这里就单单来个3作为上限了。    说在简单点就是剪枝了
部分的递归路径。    之后就是几个错误情况，先排除出去。对于正确的长度就是再一次的用if细化，还要注意s_in+l的越界问题，越界
无非是sav_in为3或是不为3，前者是正常路径，后者返回到上层递归。  bug多数是在题意的理解：它说是s.length<=3000，我以为是
给一段长度的字符串从中不断的获取ip地址呢。二是越界的处理，res.append（）什么时候执行。   测试这回也有不错的表现，感觉是最
容易出问题的几个'0011100','0011800'的结果都是正确的。
官方题解:代码没有我的x剪枝的写法。不过它的突出优点就是通过一个SEG_COUNT变量使得假如你是ipv6的ip地址也可以用，通用性非常好。
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT

        def dfs(segId: int, segStart: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return

            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if segStart == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)

            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break


        dfs(0, 0)
        return ans
'''
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        le = len(s)
        sav = [0]*4
        res = []
        if le > 12 or le < 4:
            return []
        def child(s_in, sav_in):
            x = le-(3*(3-sav_in))-(s_in)
            if x > 3:
                return False
            if x < 1:
                x = 1
            # print('x:', x)
            for l in range(x, 4):
                # 判断后续的长度，判断首字母，判断字符串小于'255',进入下个循环或是返回空列表或是递归
                if s[s_in] == '0':
                    if l != 1:
                        return False
                elif int(s[s_in:s_in+l]) > 255:
                    return False
                if s_in+l < le:
                    if sav_in < 3:
                        sav[sav_in] = s[s_in:s_in+l]
                        child(s_in+l, sav_in+1)
                else:
                    # print('sav:', sav)
                    sav[sav_in] = s[s_in:s_in + l]
                    if sav_in == 3:
                        res.append('.'.join(sav))
                    return

        child(0, 0)
        return res

a = Solution()
mt = ["25525511135", '0000', '1111', "010010", "101023", '0011800', '001110']
for i in mt[:]:
    print('in:', i)
    print(a.restoreIpAddresses(i))

'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        le = len(s)
        sav = [0]*4
        res = []

        def child(s_in, sav_in):
            for i in range(3):
                if s_in+i > le-1:
                    return False
                if i == 0 and s[s_in] == '0':
                    sav[sav_in] = '0'
                elif '255' >= s[s_in:s_in + i + 1] > '0' != s[s_in]:
                    sav[sav_in] = s[s_in:s_in+i+1]
                else:
                    return False
                if sav_in < 3:
                    child(s_in+i+1, sav_in+1)
                else:
                    res.append('.'.join(sav))
            return False

        for j in range(le-3):
            child(j, 0)
        return res
'''