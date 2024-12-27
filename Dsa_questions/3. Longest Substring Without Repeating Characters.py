class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i  =0
        unique = set()
        maxlen= 0
        for j in range(len(s)):
            while s[j] in unique:
                unique.remove(s[i])
                i+=1
            unique.add(s[j])
            maxlen = max(maxlen,j-i+1)
            
        return maxlen
                
