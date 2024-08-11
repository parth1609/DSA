class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        arr.sort()
        count  = 0
        # i, j ,k
        for  k in range(n-1,1,-1):
            j = k-1
            i = 0
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += j-i
                    j-=1
                else:
                    i+=1
        return count 
