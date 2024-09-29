
class Solution:
    def totalCount(self, k, arr):
        # code here
        sum_count = 0
        for num in arr:
            sum_count += (num + k - 1) // k
        return sum_count 
