class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = 0
        while left <= right:
            time = 0
            mid = (left + right) // 2
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)
            if time > h:
                left = mid + 1
            elif time <= h:
                answer = mid
                right = mid - 1
        
        return answer