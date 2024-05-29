class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""
        for char in path + "/":
            if char == "/":
                if res == "..":
                    if stack: stack.pop()
                elif res != "" and res != ".":
                    stack.append(res)
                res = ""
            else:
                res += char
               

        return ("/" + '/'.join(stack))
        