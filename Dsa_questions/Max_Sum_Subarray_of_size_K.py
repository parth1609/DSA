# Max Sum Subarray of size K

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i,j  = 0, 0
        total = 0
        max_sum=0
        while j < N:
            total += Arr[j]
            if (j-i+1) < K:
                j+=1
            elif (j-i+1) == K:
                max_sum = max(max_sum,total)
                total -= Arr[i]
                i+=1
                j+=1
            
        return max_sum
