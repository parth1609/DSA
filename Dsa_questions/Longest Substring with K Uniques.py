class Solution:

    def longestKSubstr(self, arr, k):
        # code here
        n = len(arr)
        i = j = 0
        unique = {}
        maxlen = -1
        while j<n:
            if arr[j] not in unique:
                unique[arr[j]] = 1
            else:
                unique[arr[j]] += 1
            
            if len(unique) == k:
                maxlen = max(maxlen,j-i+1)
            elif len(unique) > k:
                while len(unique) > k:
                    unique[arr[i]] -= 1
                    if unique[arr[i]] == 0:
                        unique.pop(arr[i])
                    i+=1
            j+=1
        return maxlen
