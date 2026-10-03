class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        difference = set()
        for i in range(n):
            difference.add(nums[i])

        for i in range(n):
            diff = target - nums[i]
            if diff in difference:
                for j in range(i+1, n):
                    if nums[j] == diff:
                        return [i, j]
                

            
                