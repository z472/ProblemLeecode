'''

我最初版本漏解了一些东西。不能处理'3214'和'32'这样的字符。是我算法的抽象程度不足导致。后来也发现了解法。
想到了但却并不好做，因为修改比较运算要触及sort(key= fucn1)的关键字key，文档说它是提供一个  可传单个参数函数 把
List中每个值都调用一遍然后比较 函数返回值。思路分析出，对于比较'3217'和'32'这样的字符，最好的还是修改 “比较” 的概念。

下面是力扣官方的代码:以下都是推测，没有更好的信息。
重载这种python官方的函数
·为什么写个类。继承str类从而重载它的__lt__方法。
·逻辑：1.只重载了小于运算，因为sorted(reverse=False)默认是降序。难道它稳定排序过程中只用到  小于  运算？
        答：在CSDN里看到确实是。但更具体说是，不论是否是降序or升序，它都是调用的__lt__
        https://blog.csdn.net/qq_35531549/article/details/88405224
        中的例子。
        Student.__lt__ = lambda self, other: self.age < other.age
        sorted(student_objects)
        结果：[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

        这里虽然它没写key关键字，但是默认是调用Student类的比较方法。就像这道题是默认走的str类的。
        这道题也可以模仿它来像官方题解里那样key=类引用（我测过那个自建的类不是可调用对象，没有__call__方法）
      2.注意写的是小于运算，如果调用了<符号大概率会无限递归自己。所以它用了>来表达意思。
      3.返回值应该是bool
      4.仅有一行，内容无错误，无遗漏，虽然内存占用可能不低，但是非常优雅。
      5.对于sorted函数：官网里，key接受单参数函数等等内容。
'''
from typing import List


class LargerNumKey(str):    # 继承了str
    # 重载了小于<  这个运算。
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))     # 即使像上面的解释了一下，但key还是像一个bug操作
        return '0' if largest_num[0] == '0' else largest_num

print('__call__' in dir(LargerNumKey))


mt = ['68', '690', '6', '6', '6', '6', '637']
bug = [111311, 1113]
superbug = [3211, 321, 32, 3]
# 它们都是我认为上升的数据，我算法没有对他们进行处理。他们有联系，大的数据靠的是长度，而不是真正的数字大
# 其实等价变换下就是长出去的部分要和自己前面部分进行字符串比大小。因为二者其实都可以作为串首。
# 不过对于循环还有要考虑的地方。
# print(Solution().largestNumber(bug))

'''
代码写的很不错，虽然逻辑漏了部分内容，但是可以保存。测试用例通过数：212 / 229
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums = [str(i) for i in nums]
        snums.sort(reverse=True)
        print(snums)
        # '68','667','637','6'...个位的'6'该如何加呢？
        # 加在 下降 字符。即不同于循环字符6的紧挨的字符是大于等于or小于6。这样的字符的前面。
        i, lensums = 0, len(snums)
        while i < lensums:
            tag, fallsum, singlesum = snums[i][0], 0, 0
            while i < lensums and tag == snums[i][0]:
                if snums[i] <= len(snums[i]) * snums[i][0]:
                    if len(snums[i]) > 1:
                        fallsum += 1
                    else:
                        singlesum += 1
                i += 1

            snums[i - fallsum:i], snums[i - fallsum - singlesum:i - fallsum] = \
                snums[i - fallsum - singlesum:i - singlesum], snums[i-singlesum:i]

        return ''.join(snums)
'''