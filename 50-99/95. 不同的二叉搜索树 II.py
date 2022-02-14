'''
你的算法对于过程的是错误的，部分地方类似于正确递归，传参的前两个和第一层的for循环。但是我的算法的结果和我
理想的测试结果仍然是不同的。分析是源自于传参的问题，把3作为测试用例作为输入，中序遍历后结果会出现4个[1,2,3]
正确的结果应是5个。有趣的是，我发现即使是不同的二叉搜索树，它的中序遍历结果都是一样的，但在95+.显示输出二叉搜
索树中，发现使用先序遍历（先中后都是指根节点的输出次序）可以显示输出这些二叉树，下面输出也用到了该遍历。
        它也表明了，我的解法是不仅有漏解也有重复解，死的透透的。即使是在3这样小的输入中。
        递推式其一： C(n+1) = C0*Cn+C1*C(n-1)+C2*C(n-2)+···+Cn*C0
有点题解指出，该题是符合“组合数学”中的--Catalan。它是一个序列，满足一个组合数该递推式网上的符号C几几和排列组
合的组合没有关系，仅表示递推式的第几项。右侧为本算法模拟的步骤，也是双重循环的原因。  而你只想出了传参的两个边
界，你的漏解就是不符合递推式的原理。你的算法的回退是每次先由根节点确定(可能也没有)做树，然后把右树的所有可行解
走到底就加入res中。没能和左树组合起来。py3传参从这里看还是很有错误的。重复解原因：要不要分析错误代码的错误逻辑。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None: continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res


# 以下是官方代码，两方面的运行表现都优于70%的提交。高效的离谱。
class Solution1:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []


print(len(Solution1().generateTrees(8)))
# for i in Solution1().generateTrees(3):
#     print(Solution2().inorderTraversal(i))
'''
逻辑错误。
class Solution1:
    def generateTrees(self, n: int) -> List[TreeNode]:
        sav = 1
        res = []
        global head
        def child(mi, ma, p) -> None:
            # p上一级递归结点，来把当前值往上面挂。由于是从上层传到下层的，范围内的值必没有用过
            # 当范围>1，就递归；否则就返回。 sav的维护，返回的位置，能否遍历尽所有解。
            nonlocal sav
            for i in range(mi, ma):
                sav += 1
                if p.val == ma:
                    p.left = TreeNode(i)
                    t = p.left
                else:
                    p.right = TreeNode(i)
                    t = p.right
                if sav == n:
                    sav -= 1
                    res.append(head)
                    return
                child(mi, i, t)
                child(i + 1, ma, t)
                sav -= 1
            return

        for j in range(1, n + 1):
            head = TreeNode(j)
            child(1, j, head)
            child(j + 1, n + 1, head)

        return res
'''
