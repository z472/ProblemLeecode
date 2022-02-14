'''
下面是官方题解最优的解法，用到str类型的isalnum()方法来判断是否是数字或是字母
但是tc仅仅比我的第二种方法好一点，但sc却比我要高4MB。且都是些优于30%的表现
来个速度快的：36ms，快于99.47%；sc也比官方要小，超过23%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #将字符串全部变为小写
        s = s.lower()
        a = []
        #如果是字母或者数字，添加到数组元素中
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                a.append(i)
        #比较顺序跟逆序，返回结果
        return(a[::1]==a[::-1])
占用少的版本：
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not ('0' <= s[l] <= '9' or 'a' <= s[l] <= 'z'):
                l += 1
            elif not ('0' <= s[r] <= '9' or 'a' <= s[r] <= 'z'):
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
欣赏一下就好。
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True


mt = ["A2 man, a plan, a canal: Panam2a", ' 2  ']
for i in mt:
    print(Solution().isPalindrome(i))
