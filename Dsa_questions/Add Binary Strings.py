
class Solution:
	def addBinary(self, s1, s2):
	    s1 = s1.lstrip('0')[::-1]
		s2 = s2.lstrip('0')[::-1]
		
		i = 0
        carry = 0
        ans = []
        n = max(len(s1), len(s2))
		while i<n:
		    a = s1[i] if i<len(s1) else 0
		    b = s2[i] if i<len(s2) else 0
		    total = int(a) + int(b) + carry
		    if total >= 2:
		        carry = 1
		    else:
		        carry = 0
		    
		    if total == 1 or total == 3:
		        ans.append('1')
		    else:
		        ans.append('0')
		    i+=1
		 
	    if carry == 1:
	        ans.append('1')
	    return ''.join(ans[::-1])
