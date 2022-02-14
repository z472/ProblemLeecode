# 题目虽然是设计个类，但可以转化成 k 个有序列表的合并出一个长度最大为10的有序列表。
# 且要求 1.不能修改那几个有序列表  2. k会是变化的

# 我没实现，但看了官方题解，思路无差。然后有个收获。就是defaultdict()声明这里应该是一个类，
# 然后默认字典类会自动调用该类的构造函数来在没有key的时候，给新的key赋值为那个构造方法。这里
# 就是d10类和 self.ustw = defaultdict(d10) 测试过是对的。其他写法是错的。
from collections import defaultdict,deque

class d10(deque):
    def __init__(self,):
        super().__init__(maxlen=10)

class Twitter:
    def __init__(self):
        self.time = 0
        self.ustw = defaultdict(d10)
        self.usfo = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.usfo[userId].add(userId)   # 发了推特同时关注自己
        self.ustw[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news10 = self.ustw[userId]
        lennews10 = 0
        for followerid in self.usfo[userId]:
            last = 0
            for j in self.ustw[followerid]:
                if lennews10 <= 10:
                    news10.append(j)
                    lennews10 += 1
                else:
                    for idx in range(last+1, 10):
                        if news10[idx] > j:
                            pass
                        # 不想写了这里可以用last保存上一个插入（满索引）的位置，因为后面的time
                        # 一定比这里大，故向后比较即可。就是这里的边界值会很丑陋。
                        # 题目是k个有序列表的合并出一个长度最大为10的有序列表


    def follow(self, followerId: int, followeeId: int) -> None:
        self.usfo[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usfo[followerId].remove(followeeId)