class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                if tokens[i] == '+':
                    result = operand1 + operand2
                    stack.append(result)
                elif tokens[i] == '-':
                    result = operand1 - operand2
                    stack.append(result)
                elif tokens[i] == '*':
                    result = operand1 * operand2
                    stack.append(result)
                else:
                    result = int(operand1 / operand2)
                    stack.append(result)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]
