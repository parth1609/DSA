class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        i = 0 # for str1
        j = 0 # for str2
        while i<m and j<n:
            if str1[i] == str2[j] or (str1[i] != 'z' and chr(ord(str1[i])+1) == str2[j]) or (str1[i] == 'z' and str2[j] == 'a'):
                j+=1
            i+=1
        return j==n
