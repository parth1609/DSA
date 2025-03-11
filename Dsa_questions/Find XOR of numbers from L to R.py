
class Solution:
    def xor_n(self,n):
        xxor = 0
        if n%4==1:
            return 1
        elif n%4==2:
            return n+1
        elif n%4==3:
            return 0
        else:
            return n
            
        return xxor
    
    def findXOR(self, l, r):
        return self.xor_n(l-1) ^ self.xor_n(r)
