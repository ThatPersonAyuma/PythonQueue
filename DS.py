import array
from collections import defaultdict
class LinkedList:
    def __init__(self, val:any=0, next:LinkedList=None):
        self.val = val
        self.next = next
        
# (Enqueue, Dequeue, Peek/Front, IsEmpty, IsFull)
class QueueArr:
    def __init__(self, initialNum: int|float, dataType: chr):
        self.arr = array.array(dataType, [0]*initialNum)
        self.capacity = initialNum  # kapasitas max
        self.size = 0               # banyak data
        self.front = 0              # indeks depan
        self.rear = -1              # indeks belakang
    def peek_front(self)->int|float:
        return self.arr[0]
    def peek_back(self)->int|float:
        return self.arr[self.rear]
    def Enqueue(self, val: int|float):
        if self.IsFull():
            raise IndexError("Queue Penuh")
        self.rear = (self.rear+1)
        self.arr[self.rear] = val
        self.size+=1
    def Dequeue(self, val: int|float):
        if self.IsEmpty():
            raise IndexError("Queue Kosong")
        self.arr = self.arr[1:] + []
        self.size -=1
    def IsEmpty(self):
        return self.size==0
    def IsFull(self):
        return self.capacity==self.size
# class QueueLS:
#     def __init__(self, initialNum: int|float):
#         self.