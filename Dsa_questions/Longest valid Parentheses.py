
class Solution:
    def maxLength(self, string):
        # code here
        stak  = [-1]
        count = 0
        for i in range(len(string)):
            if string[i] == "(":
                stak.append(i)
            elif string[i] == ")":
                stak.pop()
                if not stak:
                    stak.append(i)
                else:
                    count = max(count, i-stak[-1])
                
        return count 
