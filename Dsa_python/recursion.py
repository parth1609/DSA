'''
in Recursion if we can call the function Recursivly then thrn if we cant print 
so it shows 'segmentaion fault' which means memory is Overflow
this is also known as 'stack overflow'
'''


def printn(n):
    if n>0:
        printn(n-1)
        print(n,end=' ')
def printreverse(n):
    if n>0:
        print(n,end=' ')
        printreverse(n-1)

def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1,end=' ')

def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n,end=' ')

def printoddreverse(n):
    if n>0:
        print(2*n-1,end=' ')
        printoddreverse(n-1)

def printevenreverse(n):
    if n>0:
        print(2*n,end=' ')
        printevenreverse(n-1)

'''***************************************************'''


def sumN(n):
    if n ==1:
        return 1
    return n + sumN(n-1)
    

def sumNodd(n):
    if n ==1:
        return 1
    return (2*n-1) + sumNodd(n-1)
     

def sumNeven(n):
    if n ==1:
        return 2
    return (2*n) + sumNeven(n-1)

def fact(n):
    if n ==0:
        return 1
    return n * fact(n-1)
     

def sumsquN(n):
    if n ==1:
        return 1
    return (n*n) + sumsquN(n-1)
     
'''***********************************************'''

# multiple tecursion call
'''
# in fibbonacci list [0,1 and go forward in fibbonacci series ] 
# to get fibbonacci no. at particular Index 
[0,1] here n = 2
so next number is sum of [n-1] and [n-2] index
'''
def fibbonacci(n):
    if n<=1:
        return n
    return fibbonacci(n-1) + fibbonacci(n-2)



print(fibbonacci(2))