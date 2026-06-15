class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
            else: # char is a number
                stack.append(int(char))
        
        return stack[0]

        