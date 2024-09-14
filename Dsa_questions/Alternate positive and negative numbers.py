
class Solution:
    def rearrange(self,arr):
        # code here
        size = len(arr)
        positive = []
        negative  = []
        for i in range(size):
            if arr[i] >= 0:
                positive.append(arr[i])
            else:
                negative.append(arr[i])
                
        n,m = len(positive),len(negative)
        pos = neg = i = 0
        while pos<n and neg<m:
            if i%2==0:
                arr[i] = positive[pos]
                pos+=1
            else:
                arr[i] = negative[neg]
                neg+=1
            i+=1
        
        while pos<n:
            arr[i] = positive[pos]
            pos+=1
            i+=1
        while neg<m:
            arr[i] = negative[neg]
            neg+=1
            i+=1
        return arr
            
