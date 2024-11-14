class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def find3Numbers(self, arr, n, x):
        # Your Code Here
        arr.sort()
        for i in range(n):
            left = i+1
            right = n-1
            while left< right:
                summ = arr[i] + arr[left] + arr[right]
                if summ == x:
                    return 1
                elif summ>x:
                    right -= 1
                else:
                    left += 1
                    
        return 0
              
