class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[" or not stack:
                stack.append(i)
            elif (stack[-1] == "(" and i == ")") or (stack[-1] == "{" and i == "}") or (stack[-1] == "[" and i == "]"):
                stack.pop(-1)
            else:
                stack.append(i)
        
        return len(stack) == 0
