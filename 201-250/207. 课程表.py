from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        havedone = []
        search = {i:j for i,j in prerequisites}
        count = 0
        while count < numCourses:
            sav = []
