class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for i in range(n):
            if not stack:
                stack.append(pairs[0])
            else:
                if (target - pairs[i][0]) / pairs[i][1] <= (target - stack[-1][0]) / stack[-1][1]:
                    continue
                else:
                    stack.append(pairs[i])
        
        return len(stack)            
