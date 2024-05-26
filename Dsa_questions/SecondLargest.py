#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		last = s_last = 0
		for num in arr:
		    if num > last:
		        s_last = last
		        last = num
		    elif (last > num) and (num > s_last):
		        # last > num > s_last
		        s_last = num
        if s_last == 0:
            return -1
        else:
    return s_last
