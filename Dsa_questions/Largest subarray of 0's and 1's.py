class Solution:
    def maxLen(self, arr):
        freq = {0:-1}
        curr_sum = 0
        ans = 0
        for i in range(len(arr)):
            curr_sum += (1 if arr[i] else -1)
            if curr_sum in freq:
                ans = max(ans, i-freq[curr_sum])
            if curr_sum not in freq:
                freq[curr_sum] = i
        return ans
