class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = height[0]
        right_max = height[n - 1]
        answer = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                answer +=  right_max - height[right]

            
        return answer
