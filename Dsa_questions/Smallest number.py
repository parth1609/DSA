class Solution:
    def smallestNumber(self, s, d):
        # code here
        if s> 9*d or s<1:
            return -1
            
        result  = [0] * d
        
        for i in range(d-1,-1,-1):
            if s>9:
                result[i] = 9
                s -=9
            else:
                result[i] = s
                s = 0
                break
            
        if result[0] == 0:
            result[0] = 1
            for j in range(1,d):
                if result[j] > 0:
                    result[j] -= 1
                    break 
        return ''.join(map(str,result))
          
        
        
