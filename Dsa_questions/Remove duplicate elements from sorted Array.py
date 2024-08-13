    #User function template for Python

class Solution:

def remove_duplicate(self, A, N):
# code here
    i = 0
    for j in range(1,N):
        if A[j] != A[i]:
            i+=1
            A[i] = A[j]
    return i+1
