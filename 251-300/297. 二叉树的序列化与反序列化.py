'''
执行用时：140 ms, 在所有 Python3 提交中击败了69.54%的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了62.64%的用户
看官方题解的第一个DFS。tc,sc都是O(n)。我还是想不对路子。但是看了下题解，先序遍历还挺顺利的。
但是之后的 反序列化 就慢了些，靠的是栈存储，也多用了一半的空间来分辨是左结点还是右结点。最致命的bug来自序列化函数中的
str函数使用。后面我在创测试用例时的变量名又设成了str。直接导致错误。可能是由于类的封装，导致编辑器没有警告的提示。只有
weak warning的白色提示。错误很隐蔽。但由于开启的debug调试。能看到各个变量，传递什么的。还是很放心程序正确性的。不得不
夸它debug功能的强大易用。居然可以临时向中间加入断点。还可以切换到正常run的窗口看看输出。简直是舒适。

更快的提交：

'''
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode):
        if not root:
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        nums = data.split(',')
        head = TreeNode(int(nums[0]))
        stack = [[head, 0]]

        for i in range(1, len(nums)):
            if nums[i] != 'None':
                node = [TreeNode(int(nums[i])), 0]
            else:
                node = [None, 0]
            stack.append(node)
            if stack[-2][1] == 0:
                stack[-2][0].left = node[0]
            else:
                stack[-2][0].right = node[0]
            stack[-2][1] += 1
            while stack:
                if stack[-1][0] == None or stack[-1][1] == 2:
                    stack.pop()
                else:
                    break

        return head


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
str = Codec().serialize(root)      # bug python传统艺能了。重名的冲突。上层空间
print(str)
head = Codec().deserialize(str)
print(Codec().serialize(head))
