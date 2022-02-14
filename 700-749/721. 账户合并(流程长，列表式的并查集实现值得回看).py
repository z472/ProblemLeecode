'''
这题最初还想着自己构造哈希表去完成，后面发现，合并操作只有，只有并查集比较方便，而且并查集的指向根节点
应该是编号之类的“虚指”，我之前自己构造字典的时候，想key为每个email地址，val为返回值实体的列表地址。
但后面发现如果一个账户的emails地址集合可能对应着 多个 之前不相关(但同名)的账户，比如是{'e1':res[0],
'e2':res[0],'e3':res[1],'e4':res[1]}，出现一个账户的emails集合为'e2','e3'。我可以把'e3'的
val加到'e2'上并修改'e2','e3'对应的res列表为新的地址，但是'e1'和'e4'就无法做修改，而且这里仅仅是res[0]
有两个元素，如果它有非常多元素，那些其他的元素也要一同修改。完全不可能的。所以一定要是“虚指”，比如指向个编号(int)
这样合并只修改根节点。     为啥说流程长呢，因为并查集更新到最后，还要把每个email地址放到一个正确的列表中，还要
ascii码排序，所以还要建立个存email->账户名的字典。     下面是官方题解(py3)

对了，字符的ascii排序就是sorted()的升序，忘记了这点。
'''
import collections
from typing import List


# 这个并查集实现，纯用列表，每一个email地址为一个编号，预先知道全部结点的个数，通过list[i] == i
# 来判断是否为根结点，它就是纯纯的完成合并的逻辑，它这么写让数据和编号分离出来，它这样写让两者都非常小而清楚
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))    # 等效self.p = [_ for _ in range(n)]，第一次见这么写的

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name

        uf = UnionFind(len(emailToIndex))
        # 下面就是合并，它不考虑当前账户和的email指向什么不同的并查集，一律指向
        # 该账户第一个email地址的指向
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                uf.union(firstIndex, emailToIndex[email])

        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            # uf.find()从并查集那里可知，是找寻到根节点编号
            index = uf.find(index)
            indexToEmails[index].append(email)

        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans


