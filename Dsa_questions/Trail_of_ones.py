# Trail of ones

class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        m = 1000000007
        if n ==0:
            return 0
        fib = [0] * (n+1)
        fib[0] = 1
        fib[1] = 2
        
        for i in range(2,n+1):
            fib[i] = fib[i-1] + fib[i-2]
        
        trail = (2**n) - fib[n]
        return trail%m
