
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(string,substring, point):

            score = 0
            stack = []
            stackstring = ""
            for char in string:
                if stack and (stack[-1] + char) == substring:
                    stack.pop()
                    score += point
                else:
                    stack.append(char)
            return score, ''.join(stack)

        if x > y:
            MaxStr = "ab"
            top = x
            MinStr = "ba"
            last = y
        else:
            MaxStr = "ba"
            top = y
            MinStr = "ab"
            last = x
        
        score1, first_string = remove_substring(s,MaxStr,top)
        score2, last_string = remove_substring(first_string,MinStr,last)

        return score1 + score2
            
