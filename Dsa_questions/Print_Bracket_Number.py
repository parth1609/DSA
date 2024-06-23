# Print Bracket Number
class Solution:
  def bracketNumbers(self, str):
		# code here
		v = 0
    k =[] #  stack 
    ans = []
		for i in str:
		    if i == "(":
		        v +=1
		        k.append(v) 
            ans.append(v)
        if i == ")":
            n = k.pop()
            ans.append(n)
    return ans
                
