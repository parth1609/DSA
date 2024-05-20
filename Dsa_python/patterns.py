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
    for i in range(n+1):
        for j in range(i):
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
    
   
def pattern10(n):
    
    for i in range(1,2*n-1):
        star = i
        if i > n:
            star = 2*n-i
        for j in range(1,star+1):
            print("*",end="")
            
        print("")

def pattern11(n):
    start = 1
    for i in range(n):
        if i%2==0:
            start =1
        else:
            start = 0
        for j in range(i+1):
            print(start,end=" ")
            start = 1 - start
        print()

def pattern12(n):
    space = 2*(n-1)
    for i in range(1,n+1):
        # number
        for j in range(1,i+1):
            print(j,end="")
        # space
        for j in range(space):
            print(" ",end="")
        # number
        for j in range(i,0,-1):
            print(j,end="")
        print("")
        space-=2

def pattern13(n):
    
    for i in range(1,n+1):
        num =1
        for j in range(1,i+1):
            print(num,end=" ")
            num +=1
        print()
        
def pattern13(n):
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(j+64),end="")
        print()
        
def pattern14(n):
    
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(chr(j+64),end="")
        print()
        
def pattern15(n):
    
    for i in range(1,n+1):
        for j in range(i,i+1):
            print(chr(i+64)*j,end="")
        print()
        
        
def pattern16(n):
    for i in range(n):
        # space
        for j in range(n-i+1):
            print(" ",end="")
        # alphant
        a = ord('A')
        
        for j in range(2*i+1):
            print(chr(a),end="")
            breakpt = (2*i+1) //2
            if j < breakpt:
                a+=1 
            else:
                a-=1
        # space                         
        for j in range(n-i+1):
            print(" ",end="")
        print()
        
def pattern17(n):
    for i in range(n):
        for j in range(ord('E')-i, ord('E')+1):
            print(chr(j),end="")
        print()

        
def pattern18(n):

    iniital_spaces = 0
    for i in range(n):
        # stars
        for j in range(1,n-i+1):
            print("*",end="")
        # spaces
        for j in range(iniital_spaces):
            print(" ",end="")

        # stars
        for j in range(1,n-i+1):
            print("*",end="")
        iniital_spaces +=2 
        print()

    iniital_spaces = 8
    for i in range(1,n+1):
        # stars
        for j in range(i):
            print("*",end="")

         # spaces
        for j in range(iniital_spaces):
            print(" ",end="")
        
        # stars
        for j in range(i,0,-1):
            print("*",end="")

        iniital_spaces -=2
        print()
    

def pattern19(n):
    for i in range(1,2*n-1):
        star = i
        if i > n:
            star = 2*n-i
        for j in range(1,star+1):
            print("*",end="")
            
        print("")
    
print(pattern19(5))
