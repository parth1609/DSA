class Solution:
    def longestUniqueSubstring(self, s):
        # code here
        i= 0
        unique = {}
        maxlen = 0
        for j in range(len(s)):
            if s[j] in unique and unique[s[j]]>=i:
                i = unique[s[j]] + 1
            unique[s[j]] = j
            maxlen = max(maxlen,j-i+1)

        return maxlen

