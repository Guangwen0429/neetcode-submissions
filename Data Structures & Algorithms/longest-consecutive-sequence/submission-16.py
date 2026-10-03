class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        s = set()
        for i in range(n):
            s.add(nums[i])
        
        result = 1
        for x in s:
            count = 1
            if (x-1) in s:
                continue
            while (x+1) in s:
                count += 1
                x += 1

            result = max(count, result)

        return result