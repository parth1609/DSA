# First negative integer in every window of size k



#this is acceptable changes 

def printFirstNegativeInteger( A, N, K):
    # code here
    i = j = 0
    li = []
    ans = []
    while  j < N:
        if A[j] < 0:
            li.append(A[j])
        if (j-i+1) < K:
            j+=1
        elif (j-i+1) == K:
            if li: # if li not empty 
                ans.append(li[0])
                if A[i] == li[0]:
                    li.pop(0)
            else:
                ans.append(0)
            i+=1
            j+=1
    return ans
