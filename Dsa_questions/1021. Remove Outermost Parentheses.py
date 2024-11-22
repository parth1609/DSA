class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        k=0
        stack = []
        for bracket in s:
            if bracket == ")":
                k-=1
            if  k != 0:
                stack.append(bracket)
            if bracket == '(':
                k+=1
        return "".join(stack)                
        
