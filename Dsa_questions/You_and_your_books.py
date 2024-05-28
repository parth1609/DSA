# You and your books

class Solution:
    # Function to return the maximum number of books that can be taken
    def max_Books(self, n, k, arr):
        ans = 0
        kurr = 0
        for i in range(n):
            if arr[i] <= k:
                kurr += arr[i]
            # when the consecutive satisfy int is end 
            else:
                kurr = 0
            ans = max(ans,kurr)
        return ans
