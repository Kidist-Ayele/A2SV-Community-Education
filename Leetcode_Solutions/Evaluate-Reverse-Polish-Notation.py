from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                 x, y = stack.pop(), stack.pop()
                 stack.append(int(y / x))
            else:
                stack.append(int(char))
        return stack[0]