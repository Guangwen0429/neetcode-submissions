class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        count = {}
        length = n + m
        answer = ""
        for i in range(m):
            count[t[i]] = count.get(t[i], 0) + 1
        
        need = len(count)
        have = 0

        window = {}
        left = 0
        for right in range(n):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in count and window[s[right]] == count[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < length:
                    length = right - left + 1
                    answer = s[left: right + 1]

                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1

                left += 1
            
        return answer
                    