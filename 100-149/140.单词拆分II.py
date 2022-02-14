'''
https://leetcode-cn.com/problems/word-break-ii/solution/dong-tai-gui-hua-dfs-by-lzx1997-ih2a/
官方题解只有文字描述，而且也不清楚。他这个有很具体的讲解。全篇都粘过来了。它dfs取全部结果的函数没看，
但它前面这个“是否可以拆分”的DP推导太秀了吧。holy shit。我被秀晕了。我要是能原创把这段代码写出来就算成功。

注意理解：1.他的dp[i]是代表着前i个字符，所以要到dp[n]。  2.他的pos[i]是一个列表里面保存着前面所有可拆分的0-j-1个字符
然后是j到i-1个在wordDict里。他这个定义很绕，但就是因为这样绕，才不会漏解。也好理解后面它的dfs函数了。

与单词拆分I不同的是，这道题不仅要求判断是否可拆分，同时也需要求出拆分的结果，因此，我们我们还需要建立一个变量存储每次的状态转移过程。
动态规划求解是否可拆分，以及保留状态转移来源
记dp[i] 表示前i个字符是否可拆分，pos[i]=[j1, j2..jk]表示前i个字符可以由前j1，j2..jk以及他们之后的字符拆分。因此
状态转移方程：dp[i] = (dp[0] & s[0:i+1] in word) |......|(dp[i - 1] and s[i])
并且将其中为True的那一项对应的j添加到pos[i]中。
dfs根据pos拆分原始字符串
pos[i]记录了所有满足条件的j，即前j个字符组成的字符串可拆分且j到i的字符串在word中，因此我们可以通过深度遍历的思想访问所有情形。

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        length = 0 # 字典中最长的单词的长度
        for t in wordDict:
            length = max(length, len(t))
        wordDict = set(wordDict)
        dp = [False] * (n + 1) # 记录前i个字符是否了拆分
        pos = [[] for _ in range(n + 1)] # 记录前i个字符的状态来源
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i, i - length, -1):
                if j > 0 and s[j - 1:i] in wordDict:
                    if dp[j - 1]: # 前j个字符可拆分且第j个字符到第i个字符在字典中
                        dp[i] = True # 说明前j个可拆分
                        pos[i].append(j - 1) # 添加一条状态转移记录

        if not dp[n]: # 无法拆分
            return []

        res = []

        def dfs(start, path: str): # 深度遍历所有结果
            if start == 0: # 结束条件
                res.append(path[:-1])
            else:
                for t in pos[start]:
                    dfs(t, s[t:start] + ' ' + path) # 将每一种情况添加到path中

        dfs(n, '')
        return res

测了下它的运行表现 40ms26个测试用例，tc和sc都击败了87.8%，76.2%.
'''