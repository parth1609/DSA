class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	count = 0
    	frq = {}
    	for i in range(len(arr)):
    	    
    	    if (arr[i] + k) in frq:
    	        count += frq[arr[i] + k]
    	        
    	    if (arr[i] - k) in frq:
    	        count += frq[arr[i] - k]
        
            frq[arr[i]] = frq.get(arr[i],0) + 1
        
        return count
