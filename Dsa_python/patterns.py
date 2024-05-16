# pattern using nested loop

'''
1.for outer loop to know no. of lines rows
2. for inner loop for columns & connected them somehow to rows
3. print inside inner for loop

'''




def pattern1(n):
    for i in range(1,n+1):
        for j in range(n+1):
            print("*",end="")
        print()

def pattern2(n):
    for i in range(1,n+1):
        for j in range(i+1):
            print("*",end="")
        print()

def pattern3(n):
    for i in range(1,n+1):
        for j in range(i+1):
            print(j+1,end="")
        print()

def pattern4(n):
    for i in range(1,n+1):
        for j in range(i+1):
            print(i+1,end="")
        print()

def pattern5(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*",end="")
        print()

def pattern6(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(j+1,end="")
        print()

def pattern7(n):
    for i in range(n):
        # space
        for j in range(n-i+1):
            print(" ",end="")
        # star
        for j in range(2*i+1):
            print("*",end="")
        # space
        for j in range(n-i+1):
            print(" ",end="")
        print()


def pattern8(n):
    for i in range(n):
        # space
        for j in range(i):
            print(" ",end="")
        # star
        for j in range(2*n-(2*i+1)):
            print("*",end="")
        # space
        for j in range(i):
            print(" ",end="")
        print()

# def pattern9(n):
    
   




print(pattern7(4))
