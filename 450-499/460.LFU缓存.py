'''
这是一个很“经典”的缓存去除策略(因为缓存大小有限)

这里的get和put操作tc=O(1),sc当然就是O(n)没啥好说的。
由于是O(1)的tc基本就是考虑字典，或是哈希表(但是他它和字典不同的是要考虑哈希冲突问题)。

题目还有一点：它总提到的频率其实它给出的解释就是"次数(下面会说频率)"，即每个键值对加入数据结构后被put/get的次数。

我想法是像桶排序一样的，一个频率对应一个数组(栈)，这是为了获取但我无法做到O(1)的条件下查找某一个值。我还想过使用
一个双向链表，put到就＋1频率然后向后去到它上一个频率的链表头部，这主要还是需要遍历去寻址。

官方的算法：每一个数据都作为双向链表的结点，里面有频率和键值对还有前后结点，这操作主要是因为get为O(1)。
双向链表很好解释就是put更新后方便把该结点转移走，不破坏原来的结构。

完整的讲就是，双哈希表(其实就是字典)，一个是存key到结点(双向链表结点)地址，一个是存频率i到它同频率的一个双向链表，
每次的put和get其实也能拓展想出来了。对了，还有一个操作是LFU策略的缓存删除，要维护一个最小频率(每次put创建新的k-
v对会对它造成影响)，每次删除是删该频率对应的哈希表的表头或表尾(这看你怎么加入双向链表了)。

python没有指针，就不好去写这个存地址的逻辑，想看看它题解的写法的，，，算法伪代码都一样，但完成细节还是会看的很懵。
'''
from collections import defaultdict

class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    def insert(self, nex): # 这函数在干嘛？没有注释给我快猜吐了。
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
        return node.key

    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freqMap[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex) # 看这句话我感觉它把每个双向链表的0标记为了表头
                self.keyMap.pop(deleted)
            self.increase(node)

