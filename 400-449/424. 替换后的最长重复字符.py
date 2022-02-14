class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        滑动窗口来解决，主要是 我想的是另一个思路。单方向拓展法。tc==O( (n-k)^2 )
        但就很难再提高速度了。滑动窗口的tc==O( n )
        看了滑动窗口方法后比较了下，我的缺点是 有不必要的重复 在向右拓展的这个过程中。
        滑动窗口是用一个字典，每次的“平移”操作是O(1)，每次计算该窗口最长连续字符的tc也是O(1)

        我的方法像是把一个操作方法解决整个问题了，但滑动方法就是分部解决问题。

        此题难度不是很大。但还是那样，想的很歪，很难优化到完美上。
        '''
        pass


class SolutionOthers:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for _ in range(26)]  # 记录当前窗口的字母出现次数

        left = 0  # 滑动窗口左边界
        right = 0  # 滑动窗口右边界
        retval = 0  # 最长窗口长度

        while right < len(s):
            count[ord(s[right]) - ord('A')] += 1
            benchmark = max(count)  # 选择出现次数最多的字母为基准
            others = sum(count) - benchmark  # 则其他字母需要通过替换操作来变为基准
            if others <= k:  # 通过与K进行比较来判断窗口是进行扩张？
                right += 1
                retval = max(retval, right - left)  # 记录当前有效窗口长度
            else:  # 通过与K进行比较来判断窗口还是进行位移？
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
                right += 1  # 这里注意：位移操作需要整个向右移，不仅仅只是left向右

        return retval  # 返回最长窗口长度

