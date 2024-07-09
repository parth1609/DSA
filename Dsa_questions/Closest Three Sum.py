# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest(self, arr, target):
        n = len(arr)
        arr.sort()
        closest_sum = float('inf')
        
        for i in range(n-2):
            low = i + 1
            high = n - 1
            while low < high:
                current_sum = arr[i] + arr[low] + arr[high]
                
                if (abs(target - current_sum) < abs(target - closest_sum)) or ((abs(target - current_sum) == abs(target - closest_sum)) and current_sum > closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    low += 1
                elif current_sum > target:
                    high -= 1
                else:
                    return current_sum
        
        return closest_sum
