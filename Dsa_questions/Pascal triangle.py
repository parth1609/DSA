class Solution:
	def nthRowOfPascalTriangle(self,n):
	    ans = 1
        li = [1]
        for i in range(1,n):
            ans = ans * (n-i)
            ans = ans // i
            li.append(ans)
        return li
