
def rotate(mat): 
    #code here
    row = len(mat)
    col = len(mat[0])
    
    for i in range(row-1):
        for j in range(i,col):
            mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
    
    for i in range(row):
        mat[i].reverse()
    return mat
