class Solution:

	
	def search(self,pat, txt):
	    # code here
	    k = len(pat)
	    mapp = {}
	    for i in range(k):
	        if pat[i] not in mapp:
	            mapp[pat[i]] = 1
	        else:
	            mapp[pat[i]] += 1
	        
	    n = len(txt)
	    i = j = 0
	    count = len(mapp) 
	    ans = 0
	    while j<n:
	        if txt[j] in mapp:
	            mapp[txt[j]] -= 1
	            if mapp[txt[j]] == 0:
	                count -= 1
	            
	        if j-i+1 < k:
	            j+=1
	        
	        elif j-i+1 == k:
	            if count == 0:
	                ans += 1
	            if txt[i] in mapp:
                    mapp[txt[i]] += 1
                    if mapp[txt[i]] == 1:
                        count += 1
                    
    	        i+=1
    	        j+=1
	    
	    return ans
