'''
下面代码对于nestedList为普通的嵌套列表是对的，但原题是一个叫NestedInteger的对象。
它也是嵌套的。
题目有一个类要用那个类的方法来判断元素类型，或是递归进入它嵌套的下个对象。但核心的逻辑没
啥难度。就是下次要注意审题。
'''
class NestedIterator:
    def __init__(self, nestedList):
        self.list = []
        def cd(l):
            for i in l:
                if isinstance(i, list):     # bug
                    cd(i)
                else:
                    self.list.append(i)
        cd(nestedList)
        self.had = True if self.list else False
        self.idx = 0
        print(self.list)

    def next(self) -> int:
        ret = self.list[self.idx]
        if self.idx < len(self.list)-1:
            self.idx += 1
        else:
            self.had = False
        return ret


    def hasNext(self) -> bool:
        return self.had

mt = [[],[1,[2,[3,[4]],5],6, [7, [9,10]]], [1,[2,],3], [[1,1],2,[1,1]]]

def test(list):
    i, v = NestedIterator(list), []
    while i.hasNext():
        v.append(i.next())
    print('v:', v)

for i in mt[:]:
    print('input:', i)
    test(i)