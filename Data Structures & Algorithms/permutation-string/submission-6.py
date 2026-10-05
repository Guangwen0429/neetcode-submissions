class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        n = len(s1)
        m = len(s2)
        count1 = {}
        count2 = {}
        for i in range(n):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
        
        while right < m:
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            if right - left + 1 > n:
                count2[s2[left]] = count2.get(s2[left], 0) - 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

            if count2 == count1:
                return True

            right += 1
            
        return False 