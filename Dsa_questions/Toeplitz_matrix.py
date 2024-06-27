# Toeplitz matrix


def isToeplitz(mat):
    #code here
    n = len(mat)
    m = len(mat[0])
    
    for i in range(n-1):
        for j in range(m-1):
            if mat[i][j] != mat[i+1][j+1]:
                return False 
    return True
