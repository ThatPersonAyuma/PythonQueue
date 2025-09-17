from DS import *


my_queue = QueueArr(4, 'i')
my_queue.Enqueue(5)
my_queue.Enqueue(6)
my_queue.Enqueue(7)
my_queue.Enqueue(8)
my_queue.Dequeue()
print(my_queue.peek_back())
print(my_queue.peek_front())