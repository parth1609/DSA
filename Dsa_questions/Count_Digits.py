# Count Digits


class Solution:
    def evenlyDivides (self, N):
        i =0
        original = N
        while N>0:
		     # last_num is for extracting the each digit from the integer
            last_num = N % 10
           # if last_num is not = 0 and if last_num digit is able to divide the original number 
            if last_num != 0 and original % last_num == 0:
                i = i+1
           # this helps to get the digit from last recursively 
            N = N//10
        return i