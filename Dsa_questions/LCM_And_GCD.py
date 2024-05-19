# LCM And GCD


class Solution:
    def lcmAndGcd(self, A , B):
        # the duplicate of original var 
        # in last if section to find lcm we want multiply origninal number 
        # because is last A or B will 0 so we can't use this
        a,b = A,B
        while(A>0 and B>0):
            if A>B:
                A=A%B
            else:
                B = B%A
        if A==0:
            return [(a*b)//B,B]
        else:
            return [(a*b)//A,A]
            
