'''
执行用时：52 ms, 在所有 Python3 提交中击败了93.24%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了97.97%的用户

第一次提交，对的很莫名。
学习下好的写法。
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data: return False
        cnt = 0
        for d in data:
            if cnt == 0:
                if d >> 5 == 0b110: cnt = 1
                elif d >> 4 == 0b1110: cnt = 2
                elif d >> 3 == 0b11110: cnt = 3
                elif d >> 7 != 0:
                    return False
            else:
                if d >> 6 != 0b10: return False
                cnt -= 1
        return cnt == 0
'''
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bit = 0xFF
        b2, b5 = 0xC0, 0xF8
        data = [i & bit for i in data]
        i, lendata = 0, len(data)

        def bytetest(idx: int, bytes: int) -> bool:
            for i in range(idx + 1, idx + bytes):
                if i == lendata or (data[i] & b2) != 0x80:
                    return False
            return True

        while i < lendata:
            x = (data[i] & b5) >> 3
            if x == 0b11110 and bytetest(i, 4):
                i += 4
            elif (x >> 1) == 0b1110 and bytetest(i, 3):
                i += 3
            elif (x >> 2) == 0b110 and bytetest(i, 2):
                i += 2
            elif (x >> 4) == 0b0:
                i += 1
            else:
                return False
        return True

mt = [[197, 130, 1], [235, 140, 4], [0xF8]]
for i in mt:
    print(i, '->', Solution().validUtf8(i))