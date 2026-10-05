class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        n = len(s)
        answer = 0
        while right < n:
            count[s[right]] = count.get(s[right], 0) + 1

            while (right- left + 1) - max(count.values()) > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
             
            answer = max(answer, right - left + 1)
            right += 1
        
        return answer
        