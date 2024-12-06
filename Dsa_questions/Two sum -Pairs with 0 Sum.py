
class Solution:
    def getPairs(self, arr):
        flag = False
        if arr.count(0) > 1:
            flag = True
            
        arr = list(set(arr))
        
        if flag:
            arr.append(0)
            
        pairs = []
        n = len(arr)
        arr.sort()
        i = 0
        j = n-1
        while i<j:
            sum_ = arr[i] + arr[j]
            if sum_ == 0 :
                pairs.append([arr[i], arr[j]])
                
                i += 1
                j -= 1
                
            elif sum_ > 0:
                j-=1
                
            else:
                i += 1
            
        return pair
