class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    index = stack[-1]
                    day = i - index
                    result[index] = day
                    stack.pop()

                stack.append(i)
        
        return result
            