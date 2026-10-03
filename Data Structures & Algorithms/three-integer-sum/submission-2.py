class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = set()
        for i in range(n):
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right-= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        answers = []

        for x in result:
            answers.append(list(x))
            
        return answers