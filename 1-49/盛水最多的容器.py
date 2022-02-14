class Solution:
    def maxArea(self, height):  # height : List[int],return
        left , right = 0, len(height)-1
        newvolumn = lambda height, left, right : min(height[left], height[right])*(right-left)
        volumn = newvolumn(height, left, right)
        while True:
            if height[left] > height[right]:
                for i in reversed(range(left, right)):
                    if height[i] > height[right]:
                        right = i
                        break
                else:
                    return volumn
            elif height[left] < height[right]:
                for i in range(left+1, right):
                    if height[i] > height[left]:
                        left = i
                        break
                else:
                    return volumn
            else:
                for i in reversed(range(left, right)):
                    if height[i] > height[right]:
                        right = i
                        break
                else:
                    return volumn
                for i in range(left+1, right):
                    if height[i] > height[left]:
                        left = i
                        break
                else:
                    return volumn
                if left == right:
                    return volumn
            if newvolumn(height, left, right) > volumn:
                volumn = newvolumn(height, left, right)

h = [[1,8,6,2,5,4,8,3,7], [1,1], [1,2,1]]
a = Solution()
for i in h:
    print(a.maxArea(i))