class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        length = 0
        seen = set()
        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            length = max(length, right - left + 1)
            seen.add(s[right])
            right += 1
        
        return length
