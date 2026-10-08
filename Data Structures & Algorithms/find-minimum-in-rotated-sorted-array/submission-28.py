class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        answer = nums[0]
        while left <= right:
            if nums[left] <= nums[right]:
                answer = min(answer, nums[left])
                break
            
            mid = (left + right) // 2
            answer = min(nums[mid], answer)
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return answer