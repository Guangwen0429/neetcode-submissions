class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_width = [0] * n
        right_width = [0] * n
        stack = []
        maximum = 0

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                left_width[index] = i - index
            stack.append(i)
        
        while stack:
            index = stack.pop()
            left_width[index] = n - index
        
        for j in range(n - 1, -1, -1):
            while stack and heights[j] < heights[stack[-1]]:
                index = stack.pop()
                right_width[index] = index - j
            stack.append(j)
        
        while stack:
            index = stack.pop()
            right_width[index] = index + 1
        
        for k in range(n):
            area = heights[k] * (left_width[k] + right_width[k] - 1)
            maximum = max(area, maximum)
        
        return maximum
