class Heap:
    def __init__(self):
        self.heap  = []
    
    def createHeap(self,list1):
        for e in list1:
            self.insert(e)

    def insert(self,e):
        index = len(self.heap)
        parentIndex  = (index-1)//2
        while index > 0 and self.heap[parentIndex] < 0:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex  = (index-1)//2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] = e
    
    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]

    def Delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        tmp  = self.heap.pop()
        index =0
        leftChildIndex = (2*index)+1
        rightChildIndex = (2*index)+2

        while leftChildIndex < len(self.heap):
            if rightChildIndex < len(self.heap):
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex] > tmp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex] > tmp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index = rightChildIndex
                    else:
                        break
            else:  # no right Child
                if self.heap[leftChildIndex] > tmp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else:
                    break
            leftChildIndex = (2*index)+1
            rightChildIndex = (2*index)+2
        self.heap[index] = tmp
        return max_value
    
    def heapSort(self,list1):
        self.createHeap(list1)
        list2 = []
        try:
            while True:
                list2.insert(0,self.Delete())
        except EmptyHeapException:
            pass
        return list2


class EmptyHeapException(Exception):
    def __init__(self,msg ="Empty Heap"):
        self.msg = msg
    def __str__(self) -> str:
        return self.msg


l = [34,5,4,87,56,12,32,65]
h = Heap()
print(h.createHeap(l))
print(h.Delete())