'''
这道题我的想法是把每个子树长度计算出来，tc=O(n),然后把头结点的val存在哈希表中，
k是val,v是许多结点值，这时候因为有许多的子树长度信息，就会减少比较，只比较相同数
量的结点。但是坦白说这样实现如果root.val是相同的，比如该二叉树都是相同值，时间复杂度
并不好计算。应该介于O(n)和O(n^2)之间，可以确定，每次比较还是比较傻的要去递归查每个子
节点。     下面看下官方最优那个题解，他居然也用到了子树长度这个点，但是它的创造点就是
利用了“遍历”节点这个操作，把（节点子树值，左节点，右结点）放入哈希表作为key，value就是
它出现次数，当重复出现时就送到res。     它的写法也值得一看。
'''
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        # 当key对应的value第一次出现时赋值给value的方法
        # 这里就是第几次加入trees字典，对应值就是几，就是题解说的唯一标记嘛
        # 要注意第一次加入__len__显示的为0，很奇怪？应该是加入前的__len__，因为赋值前还没有值。
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []

        def lookup(node):
            if node:
                # 主要是靠这行靠trees字典去去重
                # 在这行断点debug左侧的Frames有很多递归函数的作用域，要分清。
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        # 在这里下断点可以看到程序最后root回退的结构
        return ans

# 在lookup递归当回退左结点上去访问右结点的时候能看到左结点的结构(看trees结构)。这里把左结点构造的复杂些，
# 因为在右子树回退时整个程序就会退出（尝试在末尾下断点解决该问题，对的）
r = TreeNode(2, TreeNode(4))
l = TreeNode(3,TreeNode(2,TreeNode(4, TreeNode(8))),TreeNode(4))
root = TreeNode(1, l, r)
print(Solution().findDuplicateSubtrees(root))