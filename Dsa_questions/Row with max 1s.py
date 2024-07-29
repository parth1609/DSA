class Solution:

	def rowWithMax1s(self,arr):
		# code here
		row = len(arr)
		kol = len(arr[0])
		
		ons_row = -1
		R = 0
		K = kol-1
		
		while R<row and K >=0:
		    if arr[R][K] == 0:
		        R+=1
		    else:
		        ons_row = R
		        K-=1
		return ons_row
