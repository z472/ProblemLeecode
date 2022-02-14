'''
执行用时：44 ms, 在所有 Python3 提交中击败了29.98%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了13.12%的用户
提交错了3次，但是debug浪费了很久，超过了写代码的时间。因为前一次是入栈，后面是出栈的问题。
下面看一个提交100%的迭代的代码20ms
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==']':
                index=stack[::-1].index('[')
                index=len(stack)-index-1
                temp=stack[index+1:]

                j=index-1
                while j>=0:
                    if stack[j]>='0' and stack[j]<='9':
                        j-=1
                    else:
                        break
                j+=1
                num=stack[j:index]
                num=''.join(num)
                num=int(num)
                temp=num*temp
                stack=stack[:j]+temp
            else:
                stack.append(i)
        return  ''.join(stack)

看过它代码的收获，怎么可以这么呆，一顿用切片，翻转切，找整数切，出栈一个然后也切。但是我提交之后看它的sc和我基本一致。

它创的栈就比我少一个，还有就是变量的使用上也少很多。
它的出栈，不用考虑把当前字符串输出给递归的返回值或是上层的栈。
逻辑的一致性很好。
我就是纯纯的根据遍历的内容做反应，相互之间的逻辑有很多纠缠部分，还要把很多变量都正确的偏移。
当然就是因为他们之间的类似状态机一样的变化。导致了很多难以察觉的bug。要具体到调试中看。

宏观上：我和他的区别就是逻辑分散和聚集的区别。这个逻辑本该是连贯的一个动作一个效果的，但我硬是给掰开了，就为了配合for的迭代。
实操中：我的if要比他多很多很多，还有许多是嵌套的if...else更是增加了理解难度，都是一个个零碎条件的映射。我改最后一个bug的时候
连当时为啥要写它都不记得了。离谱不。
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stackbracket = []
        stacknum = []
        num, strings = '', ''
        ret = ''
        for idx, i in enumerate(s):
            if '0' <= i <= '9':
                num += i
            elif 'a' <= i <= 'z':
                strings += i
            elif i == '[':
                # 这里和']'有个共用的代码，不过幸好没有第一次写的时候就放一起，要不找bug就会很难了
                if strings:
                    if stackbracket:
                        stackbracket[-1] += strings     # bug 和下面的一样，它是第二个，这是为一个情况写的。
                    else:
                        ret += strings
                    strings = ''
                stacknum.append(int(num))
                stackbracket.append('')
                num = ''
            else:  # ']'
                if strings:  # bug这种就是很常见的，把某个值默认清零之后，无意中干扰了常规操作
                    stackbracket[-1] += strings
                if len(stackbracket) > 1:
                    # bug if else
                    # if strings:   我到后面已经忘记这个语句是什么意思了，就删掉看了。
                    #     stackbracket[-2] += stacknum[-1] * strings
                    # else:
                    stackbracket[-2] += stacknum[-1] * stackbracket[-1]
                else:
                    ret += stacknum[-1] * stackbracket[-1]
                stacknum.pop()
                stackbracket.pop()
                strings = ''
        return ret + strings


mt = ["2[abc]3[cd]ef", "1[a1[c]f1[d]e]"]
bug = ["abc3[cd]xyz", "1[1[y]p1[1[j]e1[f]]]", "1[a1[b1[c]d]s]"]
for i in mt[:]+bug[:]:
    print(i, ' ', Solution().decodeString(i))
