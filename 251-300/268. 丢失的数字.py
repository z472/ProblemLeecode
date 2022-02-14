from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def XORntimes(n: int):
            sav = 0
            for i in range(n + 1):
                sav ^= i
            return sav

        n = len(nums)
        z = XORntimes(n)
        x = 0
        for i in nums:
            x ^= i
        return x^z

mt = [[3,0,1], [9,6,4,2,3,5,7,0,1]]
for i in mt:
    print(i, '->', Solution().missingNumber(i))