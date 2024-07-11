class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        string = ""

        for char in s:
            if char == '(':
                stack.append(string)
                string = ""
            elif char.isalpha():
                string += char
            else:
                string = string[::-1]
                stacktop = stack.pop()
                string  = stacktop + string
        return string
