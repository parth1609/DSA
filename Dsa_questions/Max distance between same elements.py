class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        mapp = {}
        max_ = 0
        for i in range(len(arr)):
            if arr[i] not in mapp:
                mapp[arr[i]] = i
            else:
                max_ = max(max_, i - mapp[arr[i]])
        
        return max_
