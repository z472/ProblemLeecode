from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        houses.sort()
        heaters.sort()
        if heaters[0] > houses[0]:
            res = heaters[0] - houses[0]
        if heaters[-1] < houses[-1]:
            res = max(res, houses[-1] - heaters[-1])

        idx = 0
        for i in range(len(houses)):
            if houses[i] > heaters[0]:
                idx = i
                break
        for i in range(len(heaters) - 1):
            while houses[idx] < heaters[i + 1]:
                res = max(min(houses[idx] - heaters[i], heaters[i + 1] - houses[idx]), res)
                idx += 1
                if idx == len(houses):
                    return res
        return res


test = [[1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499, 500, 501]]
t2 = [[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
      [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]]
print(Solution().findRadius(*t2))