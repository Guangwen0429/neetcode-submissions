class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        maximum = 0
        while left < right:
            contain = min(heights[left], heights[right]) * (right - left)
            maximum = max(maximum, contain)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                if (heights[left+1] - heights[left]) > (heights[right-1] - heights[right]):
                    left += 1
                else:
                    right -= 1

        return maximum