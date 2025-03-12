class Solution:
    def twoOddNum(self, Arr, N):
        nums = 0
        for num in Arr:
            nums = nums ^ num
        rightmost = (nums & (nums-1)) ^ nums
        b1 = 0 #for rightmost bit  is set(1)
        b2 = 0 #for rightmost bit is not set(0)
        
        for i in range(len(Arr)):
            if (Arr[i] & rightmost):
                b1 ^= Arr[i]
            else:
                b2 ^= Arr[i]
        return [b1,b2] if b1 > b2 else [b2,b1]

