class Solution:
    def removeElement(self, nums, val) :
        n, oupt, j = len(nums), 0, -1
        for i in range(n-1):
            if nums[i] == val:
                if j == -1:
                    j = oupt
                for j in range(j,n):  # j 是上次交换时非val值的位置
                    if nums[j] != val:
                        oupt += 1
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                if j == n:
                    return oupt
            else:
                oupt += 1
        print(nums)
        return oupt

a = Solution()
test = [([3,2,2,3], 3), ([0,1,2,2,3,0,4,2], 2), ([2], 3)]
for i in test:
    print(a.removeElement(i[0], i[1]))