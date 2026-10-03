class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            while s[right] in s[left:right]:
                left += 1
            length = max(length, right - left + 1)
            right += 1
        
        return length
