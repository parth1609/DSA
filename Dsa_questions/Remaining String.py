class Solution:
	def printString(self, s, ch, count):
		# code here
		kount = 0
		string = ""
		for i in range(len(s)):
		    if s[i]== ch :
		        kount +=1
	        if kount == count:
	            string = s[i+1:]
	            break 
		    else:
    		    string =  ""
		return string
