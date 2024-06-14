# Armstrong Numbers


class Solution:
    def armstrongNumber (self, n):
        # code here 
        original = n
        total = 0
        while n != 0:
            last_num = n% 10
            total = total + (last_num ** 3)
            n = n//10
        return "Yes" if total == original else "No"
