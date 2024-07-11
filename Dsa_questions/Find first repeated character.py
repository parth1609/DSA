class Solution:

    def firstRepChar(self, s):
        # code here
        li = [0] * 26
        for i in s:
            index = ord(i) - ord('a')
            if li[index] != 0:
                return i
            li[index] +=1
        return -1
