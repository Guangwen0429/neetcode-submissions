class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n 
        prefix[0] = 1
        suffix[n-1] = 1
        result = []
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
             
        for i in range(n-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]

        for i in range(n):
            result.append(prefix[i] * suffix[i])
        
        return result