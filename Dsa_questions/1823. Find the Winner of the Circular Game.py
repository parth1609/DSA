# using array modulo method
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        i = 0
        while len(arr) > 1:
            index = (i + k -1) % len(arr)
            arr.pop(index)
            i = index
        return arr[0]

# implement with queue
import queue
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = queue.Queue()
        for i in range(1,n+1):
            arr.put(i)
        while arr.qsize() > 1:
            for count in range(k-1):
                arr.put(arr.get())
            arr.get()
        return arr.get()
