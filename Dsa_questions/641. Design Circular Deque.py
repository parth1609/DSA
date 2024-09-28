class node:
    def __init__(self,val:int):
        self.val = val
        self.next = None 
        self.prv = None 

class MyCircularDeque:

    def __init__(self, k: int):
        self.count = 0
        self.n = k
        self.front = None 
        self.rear = None 

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = node(value)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prv = new_node
            self.front = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = node(value)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prv = self.rear 
            self.rear = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False 
        if self.front == self.rear:
            self.front = self.rear = None 
        else:
            self.front = self.front.next 
            self.front.prv = None 
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False 
        if self.front == self.rear:
            self.front = self.rear = None 
        else:
            self.rear = self.rear.prv
            self.rear.next = None 
        self.count -= 1
        return True
        

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.front.val
        return -1
        
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.rear.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.n
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
