# The Palindrome Pattern


class Solution:
    def pattern (self, arr):
        # code here
        n = len(arr)
        m = len(arr[0])
        
        # for row
        for i in range(n):
            palin = ""
            for j in range(m):
                palin += str(arr[i][j])
            if palin == palin[::-1]:
                s = str(i) + " R"
                return s
        # for column      
        for i in range(n):
            palin = ""
            for j in range(m):
                palin += str(arr[j][i])
            if palin == palin[::-1]:
                s = str(i) + " C"
                return s
        return -1
                
