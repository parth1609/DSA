#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        n = len(arr1)
        m = len(arr2)
        ans = sum1 = sum2 = i = j = 0
        while i < n and j < m:
            if arr1[i] == arr2[j]:
                ans += max(sum1,sum2) + arr1[i]
                sum1 = sum2 = 0
                i+=1
                j+=1
            elif arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            else:
                sum2 += arr2[j]
                j+=1
        while i<n:
            sum1 += arr1[i]
            i+=1
        while j < m:
            sum2 += arr2[j]
            j+=1
        
        return ans + max(sum1, sum2)
