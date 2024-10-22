import math
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		n=len(arr)
		summ=0
		m = 1000000007
		for num in arr:
		    summ ^= num
		   
		if summ == 0:
		    return int(math.pow(2,n-1)-1) % m
		else:
		    return 0
