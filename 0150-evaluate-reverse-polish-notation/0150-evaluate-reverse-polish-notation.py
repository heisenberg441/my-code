class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                y1 = stack.pop()
                y2 = stack.pop()
                stack.append(y2 - y1)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                y1 = stack.pop()
                y2 = stack.pop()
                stack.append(int(y2 / y1))
            else:
                stack.append(int(i))
        
        return stack[0]
  