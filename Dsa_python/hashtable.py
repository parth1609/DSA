class hashfunction:
    def __init__(self,N) :
        self.N = N
        self.array =  [0] *  N
    
    
    def add_elememt(self, elememt):
        if elememt:
            index = elememt%self.N 
            self.array[index] = elememt
        else:
            return "NULL"
    
    def search_elememt(self,elememt):
        if elememt:
            index = elememt%self.N 
            if self.array[index] == elememt:
                return True
            else:
                return False
        else:
            return "NULL"
    
    def delete_elememt(self,elememt):
        if self.array:
            index = elememt%self.N 
            if self.array[index] == elememt:
                self.array[index] = 0
            

    def print_hashtable(self):
        return self.array
        
    
    
# o/p
# [0, 0, 0, 0, 88, 0]
# [0, 0, 8, 0, 88, 0]


hash = hashfunction(6)
print(hash.add_elememt(88))
print(hash.add_elememt(17))

print(hash.print_hashtable())
