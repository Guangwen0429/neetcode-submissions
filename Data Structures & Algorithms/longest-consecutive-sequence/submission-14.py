class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        new_nums = set()
        new_nums_copy = set() 
        for i in range(n):
            new_nums.add(nums[i])
            new_nums_copy.add(nums[i])
        
        result = 1
        for x in new_nums:
            count = 1
            if (x-1) in new_nums_copy:
                continue
            while (x+1) in new_nums_copy:
                count +=1
                new_nums_copy.discard(x+1)
                x += 1
            result = max(result, count)
        
        return result