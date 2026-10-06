class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        output = []
        right = 0

        while right < n:
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if q[0] < right - k + 1:
                q.popleft()
            
            if right >= k - 1:
                output.append(nums[q[0]])
            
            right += 1

        return output


