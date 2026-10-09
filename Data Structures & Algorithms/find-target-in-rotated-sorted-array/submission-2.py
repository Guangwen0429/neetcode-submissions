class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        start = left 
        end = (left +len(nums) - 1)

        while start <= end:
            middle = (start + end) // 2
            index = middle % len(nums)
            if nums[index] == target:
                return index
            else:
                if nums[index] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            
        return -1

