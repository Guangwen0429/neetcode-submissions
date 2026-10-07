class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspond = {')':'(', ']':'[', '}':'{'}
        n = len(s)
        count = 0
        while count < n:
            ch = s[count]
            if ch in correspond:
                if stack and correspond[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
            
            count += 1
                
        return not stack 