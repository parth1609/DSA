# Count numbers containing 4

class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        four = 0
        for i in range(1,n+1):
            if '4' in str(i):
                four +=1
                
        return four
