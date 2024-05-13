from math import log10

#  TC is (log10(n))
def count_using_log10(N):
    while N>0:
        # n = 235 
        # let log10(235) = 2.37 = 2.37+1 = int(3.37) = 3
        # so total count is 3
        return int(log10(N))+1
    

# TC if O(n)
def nums(N):
    i =0
    while(N > 0 ):
        i = i+1
        N = N // 10
    return i
        

def extract_all_num(N):
    li = []
    while(N > 0 ):
        last_num = N % 10
        li.append(last_num)
        N =N // 10
    return li
    # return  [i for i in map(int,li) ]



def reverse(N):
    rvrs_no = 0
    while(N > 0 ):
        last_num = N % 10
        # 235
        # 1. last_num = 5, so rvrs_no = (0*10)+5 = 5
        # 2. last_num = 3, so rvrs_no = (5*10)+3 = 53
        # 3. last_num = 2, so rvrs_no = (53*10)+2 = 532
        rvrs_no = (rvrs_no * 10 ) + last_num
        N =N // 10
    return rvrs_no
    # return  [i for i in map(int,li) ]


def palindrome(N):
    duplicate = N
    reverse_no = 0
    while(N > 0 ):
        last_num = N % 10
        reverse_no = (reverse_no * 10 ) + last_num
        N =N // 10
        # not able to compare with N becasuse ' N will 0 at last while extraction'
        # so we compare with duplicate which is copy of N
        #  variabl duplicate is becasuse of to save the copy of original No.
    return True if reverse_no == duplicate else False


def armstrong_num(N):
    # N = 371
    # after extracting number is "last_num", 
    # 1. last_num = 1, so 1**3 = 1 then total = 0 + 1 = 1
    # 2. last_num = 7 so 7**3 = 343 then total = 1 + 343 = 344
    # 3. last_num = 3 so 3**3 = 27 = then  total = 344 + 27 = 371 
    duplicate = N
    total = 0
    while(N > 0 ):
        last_num = N % 10
        total = total + (last_num ** 3)
        N =N // 10
    return True if total == duplicate else False
        

# TC of O(n)
def divisor_of_number(N):
    li = []
    for i in range(1,N+1):
        if N%i==0:
            li.append(i)
    return li

# TC of O(sqrt(n))
def divisor_of_Pnumbers(N):
    # In this function , the loop is not check whole divisors of given number 
    # But it only checked half of it 
    # because after half, the numbers are repeated
    '''
    [1 x 12]
    [2 x 6]
    [3 x 4]
    from now the divisor are repeating 
    [4 x 3]
    [6 x 2]
    [12 x 1]
    '''
    # TC of O(sqrt(n))
    li = []
    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            li.append(i)
            if N%i != i:
                li.append(N//i)
                
    return sorted([i for i in li])

# [1, 2, 3, 4, 6, 6.0, 9.0, 12.0, 18.0, 36.0]



def prime_nums(N):
    count = 0
    # TC of O(n)
    # this loop check go through all the divisors 
    # which increases Time
    for i in range(1,N+1):
        if N%i==0:
            count = count+1

    return True if count==2 else False 

def prime_num(N):
    # In this function , the loop is not check whole divisors of given number 
    # But it only checked half of it 
    # because after half, the numbers are repeated

    count = 0
    for i in range(1,N+1):
        if N%i == 0:
            count = count+1
            if N%i != i:
                count = count+1
    return True if count==2 else False 

# Greatest_common_divisor or Highest_common_factor 
# by linear method
def Greatest_common_divisor(n1,n2):
    # TC of O(min(n1,n2))  means O(n) 
    for i in range(1, min(n1,n2)):
        # if the int which divides both number return that int  
        if n1%i==0 and n2%i==0:
            return i
        

# by Euclidon algorithm

# it states that gcd(a,b) = gcd(a-b,b) where a>b
# but for large numbers this will never beat the linear way

# so gcd(a,b) = gcd(a%b,b) where a>b
# it is the same algorithm but just changes mathmatical way to more efficient way 
def Greatest_common_divisor_by_Euclidon_algorithm(a,b):
    # TC of O(logphi(min(a,b)))
    while (a>0 and b>0):
        if a >b:
            a = a%b
        else:
            b = b% a
    return b if a == 0  else a
         


        
a = prime_num(11)
print(a)