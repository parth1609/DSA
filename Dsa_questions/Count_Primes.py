# Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=1:
            return 0
        prime = [True] * (n+1)
        prime[0] = prime[1] = False 

        result = []
        for i in range(2,n+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j] = False
        count = 0
        for p in prime:
            if p == True:
                count += 1
        return count -1
        

