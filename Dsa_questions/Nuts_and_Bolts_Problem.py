# Nuts and Bolts Problem

class Solution:
    def matchPairs(self, n, nuts, bolts):
        # Helper function to sort using Quick Sort
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[0]
                left = [x for x in arr if x < pivot]
                right = [x for x in arr if x > pivot]
                return quick_sort(left) + [pivot] + quick_sort(right)
                
        sorted_nuts  = quick_sort(nuts)
        sorted_bolts  = quick_sort(bolts)
        
        # Assign the sorted values back to the original lists
        for i in range(n):
            nuts[i] = sorted_nuts[i]
            bolts[i] = sorted_bolts[i]
                
