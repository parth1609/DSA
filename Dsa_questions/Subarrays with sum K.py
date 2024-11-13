from collections import defaultdict
class Solution:
    def findSubArraySum(self, k, arr):
        n = len(arr)
        count = 0
        prefix_sum = 0
        hashmap = defaultdict(int)
        
        hashmap[0] = 1
        for i in range(n):
            prefix_sum += arr[i]
            remaining_sum = prefix_sum - k
            count += hashmap[remaining_sum]
            hashmap[prefix_sum] += 1
        return count
            
