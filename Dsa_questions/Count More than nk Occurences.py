from collections import Counter
class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        count = Counter(arr)
        a = 0
        for i in count.values():
            if i > n//k:
                a+=1
        
        return a
                
