class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        buckets = [[] for _ in range(n+1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                if len(result) == k:
                    return result
                result.append(num)
        return result