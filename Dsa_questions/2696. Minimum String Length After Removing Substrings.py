class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue 
            if stack[-1] == "A" and char == "B":
                stack.pop()
            elif stack[-1] == "C" and  char == "D":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
            
