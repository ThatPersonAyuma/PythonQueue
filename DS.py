import array
from enum import Enum
class LinkedList:
    def __init__(self, val:any=0, next:"LinkedList"=None): # Use string instead of data type cause Python didn't know it yet
        self.val = val
        self.next = next
class TravelTrait:
        def travel(node: LinkedList, index: int):
            if (index<0):
                raise IndexError("Index Can't be A Negative Number")
            current = node
            while(index>0 and current.next!=None):
                current = current.next
                index-=1
            if index!=0:
                raise IndexError("Out of Range")
            node.val = current.val      # Use this to do inplace but return it if don't
            node.next = current.next
# (Enqueue, Dequeue, Peek/Front, IsEmpty, IsFull)
class QueueArr:
    def __init__(self, Max, dataType: chr='i'):
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
    
class QueueCircle:
    def __init__(self, Max, dataType: chr='i'):
        self.arr = array.array(dataType, [0]*Max)
        self.capacity = Max  # kapasitas max
        self.size = 0               # banyak data
        self.front = 0              # indeks depan
        self.rear = -1              # indeks belakang
    def peek_front(self)->int|float:
        if(self.size==0):
            return None
        return self.arr[self.front]
    def peek_back(self)->int|float:
        if(self.size==0):
            return None
        return self.arr[self.rear]
    def Enqueue(self, val: int|float):
        if self.IsFull():
            raise IndexError("Queue Penuh")
        self.rear = (self.rear+1)%self.capacity
        print(f"{val} ada di indeks: {self.rear}")
        self.arr[self.rear] = val
        self.size+=1
    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue Kosong")
        self.front=(self.front+1)%self.capacity
        print(f"Indeks front: {self.front}")
        self.size -=1
    def IsEmpty(self):
        return self.size==0
    def IsFull(self):
        return self.capacity==self.size
    
class PriorityQueue:
    def __init__(self, Max: int):
        self.capacity = Max         # kapasitas max
        self.size = [0,0,0]         # banyak data, format [low, mid, high]
        self.front:LinkedList=None
        self.rear:LinkedList=None
        # self.front = 0              # indeks depan
        # self.rear = -1              # indeks belakang
    def peek_front(self)->int|float:
        if(sum(self.size)==0):
            return None
        return self.front.val
    def peek_back(self)->int|float:
        if(sum(self.size)==0):
            return None
        return self.rear.val
    def Enqueue(self, item:"PriorityItem"):
        if self.IsFull():
            raise IndexError("Queue Penuh")
        if self.IsEmpty():
            self.front=LinkedList(val=item.val)
            self.rear=self.front
        else:
            from_back = sum(self.size[:item.priority.value])
            from_front = sum(self.size)-from_back
            if (from_back==0):
                self.rear.next = LinkedList(val=item.val)
                self.rear = self.rear.next
            elif (from_front==0):
                self.front = LinkedList(val=item.val, next=self.front)
            else:
                front = self.front
                for _ in range(from_front-1):
                    front=front.next
                front.next=LinkedList(item.val, front.next)
        self.size[item.priority.value]+=1
    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue Kosong")
        self.front=self.front.next
        for i in range(3):
            if(self.size[2-i]!=0):
                self.size[2-i]-=1
                break
    def IsEmpty(self):
        return sum(self.size)==0
    def IsFull(self):
        return self.capacity==sum(self.size)
    def get_items(pr_queue: "PriorityQueue"):
        result=[]
        if pr_queue.IsEmpty():
            return result
        front = pr_queue.front
        while(front.next!=None):
            result.append(front.val)
            front=front.next
        result.append(front.val)
        return result
    class PriorityItem:
        class Priority(Enum):
            LOW = 0
            MID = 1
            HIGH = 2
        def __init__(self, val: int|float, priority: Priority):
            self.val = val
            self.priority = priority