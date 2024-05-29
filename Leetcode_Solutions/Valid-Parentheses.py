class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen = { ")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in closeToopen:
                if stack and stack[-1] == closeToopen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
           

        