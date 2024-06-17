# 633. Sum of Square Numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0
        b = int(c**0.5)

        while a<=b:
            square_sum = a*a + b*b
            if square_sum == c:
                return True
            elif square_sum < c:
                a+=1
            else:
                b-=1
        return False 
