class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        answer = max(nums)
        while left <= right:
            if nums[left] <= nums[right]:
                answer = min(answer, nums[left])
                break
            mid = (left + right) // 2
            answer = min(answer, nums[mid])
            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return answer
