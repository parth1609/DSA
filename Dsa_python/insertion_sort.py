def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while (j>0 and arr[j-1] > arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr

l = [4,5,2,45,56,76,9,1]
print(insertion_sort(l))