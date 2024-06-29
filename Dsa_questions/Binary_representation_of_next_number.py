# Binary representation of next number

#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
		n =  (int(s, 2))+1
    return bin(n)[2:]
