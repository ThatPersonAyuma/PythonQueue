import array
class LinkedList:
    def __init__(self, val:any=0, next:"LinkedList"=None): # Use string instead of data type cause Python didn't know it yet
        self.val = val
        self.next = next
    def travel(self, index: int):
        if (index<0):
            raise IndexError("Index Can't be A Negative Number")
        current = self
        while(index>0 and current.next!=None):
            current = current.next
            index-=1
        if index!=0:
            raise IndexError("Out of Range")
        self.val = current.val  # Use this to do inplace but return it if don't
        self.next = current.next
# (Enqueue, Dequeue, Peek/Front, IsEmpty, IsFull)
class QueueArr:
    def __init__(self, Max: int=0, dataType: chr='i'):
        self.arr = array.array(dataType, [0]*Max)
        self.capacity = Max  # kapasitas max
        self.size = 0               # banyak data
        self.front = 0              # indeks depan
        self.rear = -1              # indeks belakang
    def peek_front(self)->int|float:
        if(self.size==0):
            return None
        return self.arr[0]
    def peek_back(self)->int|float:
        if(self.size==0):
            return None
        return self.arr[self.rear]
    def Enqueue(self, val: int|float):
        if self.IsFull():
            raise IndexError("Queue Penuh")
        self.rear += 1
        self.arr[self.rear] = val
        self.size+=1
    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue Kosong")
        self.arr = self.arr[1:] + array.array(self.arr.typecode, [0])
        self.rear-=1
        self.size -=1
    def IsEmpty(self):
        return self.size==0
    def IsFull(self):
        return self.capacity==self.size
class QueueLS:
    def __init__(self, Max: int):
        self.capacity = Max
        self.size = 0
        self.front:LinkedList=None
        self.rear:LinkedList=None
    def peek_front(self)->int|float:
        if(self.front==None):
            return self.front
        return self.front.val
    def peek_back(self)->int|float:
        if(self.rear==None):
            return self.rear
        return self.rear.val
    def Enqueue(self, val: int|float):
        if self.IsFull():
            raise IndexError("Queue Penuh")
        if self.IsEmpty():
            self.front=LinkedList(val=val)
            self.rear=self.front
        else:
            self.rear.next=LinkedList(val=val)
            self.rear=self.rear.next
        self.size+=1
    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue Kosong")
        self.front=self.front.next
        if(self.front==None):
            self.rear=None
        self.size -=1
    def IsEmpty(self):
        return self.size==0
    def IsFull(self):
        return self.capacity==self.size