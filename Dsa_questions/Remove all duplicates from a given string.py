class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    alphabets  = {}
	    for i in range(len(s)):
	        if s[i] in alphabets:
	            continue
	        alphabets[s[i]] = 1
	    return ''.join(list(alphabets))
