'''
执行用时：24 ms, 在所有 Python3 提交中击败了97.84%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.25%的用户

知道这题是麻烦的字符串处理，想写的简洁点，练习0.1%的代码能力。结果就是错了7次。
'''
import string
class Solution:
    def validIPAddress(self, IP: str) -> str:
        judge = lambda allow,strs : (not strs or [_ for _ in strs if _ not in allow])
        if '.' in IP and IP.count('.') == 3:
            for i in IP.split('.'):
                if judge(string.digits, i) or (i[0] == '0' and i != '0') or not ( 0<= int(i) <= 255):
                    return 'Neither'
            return 'IPv4'
        elif ':' in IP and IP.count(':') == 7:
            xallows = string.digits+'abcdefABCDEF'
            for i in IP.split(':'):
                if len(i)>4 or judge(xallows, i):
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'