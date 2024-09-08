
class Solution:
    def findNth(self,n):
        #code here
        result = 0
        base = 1
        
        while n>0:
            result += (base  * (n%9))
            n = n // 9
            base = base * 10
        return result 
            
