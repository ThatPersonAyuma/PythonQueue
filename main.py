from DS import *
# region Use of Deque
my_deque = Deque(4)
my_deque.Enqueue(1)
my_deque.Enqueue(2)
my_deque.Enqueue(3, True)
print(my_deque.arr)
print(my_deque.peek_front())
my_deque.Dequeue(False)
print(my_deque.arr)
my_deque.Enqueue(4)
my_deque.Enqueue(5, True)
print(my_deque.arr)
my_deque.Dequeue(False)
my_deque.Dequeue(False)
my_deque.Dequeue()
my_deque.Enqueue(6, True)
my_deque.Enqueue(7)
print(my_deque.arr)
print(my_deque.peek_front(), my_deque.peek_back())
# endregion
# region shorhand
PI = PriorityQueue.PriorityItem
# endregion
# region Use of PriorityQueue
my_priority_queu = PriorityQueue(5)
my_priority_queu.Enqueue(PI(1, PI.Priority.LOW))
print(my_priority_queu.peek_front(),my_priority_queu.peek_back())
my_priority_queu.Enqueue(PI(2, PI.Priority.HIGH))
print(my_priority_queu.peek_front(),my_priority_queu.peek_back())
my_priority_queu.Enqueue(PI(3, PI.Priority.MID))
print(my_priority_queu.peek_front(),my_priority_queu.peek_back())
my_priority_queu.Enqueue(PI(4, PI.Priority.HIGH))
my_priority_queu.Dequeue()
print(my_priority_queu.peek_front(),my_priority_queu.peek_back())
my_priority_queu.Enqueue(PI(5, PI.Priority.MID))
print(PriorityQueue.get_items(my_priority_queu))
print(PriorityQueue.get_items(my_priority_queu))
print(PriorityQueue.get_items(my_priority_queu))
# endregion
# region Use of QueueCircle
# my_queue_circle = QueueCircle(Max=4)
# my_queue_circle.Enqueue(1)
# my_queue_circle.Enqueue(2)
# my_queue_circle.Enqueue(3)
# my_queue_circle.Enqueue(4)
# print(my_queue_circle.peek_front())
# my_queue_circle.Dequeue()
# print(my_queue_circle.peek_front())
# my_queue_circle.Enqueue(5)
# my_queue_circle.Dequeue()
# print(my_queue_circle.peek_front())
# my_queue_circle.Enqueue(6)
# print(my_queue_circle.peek_front())
# print(my_queue_circle.peek_back())
# endregion
# region Use of QueueLS
# my_queue_ls = QueueLS(4)
# my_queue_ls.Enqueue(2)
# my_queue_ls.Enqueue(5)
# print(my_queue_ls.peek_back())
# print(my_queue_ls.peek_front())
# my_queue_ls.Dequeue()
# print(my_queue_ls.peek_back())
# print(my_queue_ls.peek_front())
# my_queue_ls.Dequeue()
# print(my_queue_ls.peek_back())
# print(my_queue_ls.peek_front())
# endregion
# region Use of LinkedList
# my_ls = LinkedList()
# my_ls2 = my_ls
# my_ls2.next = LinkedList(2)
# my_ls2=my_ls2.next
# my_ls2.next = LinkedList(3)
# my_ls.travel(2)
# my_ls.travel(1)
# print(my_ls.val)
# endregion
# region Use of QueueArr
# my_queue = QueueArr(4, 'i')
# my_queue.Enqueue(5)
# my_queue.Enqueue(6)
# my_queue.Enqueue(7)
# my_queue.Enqueue(8)
# my_queue.Dequeue()
# print(my_queue.peek_back())
# print(my_queue.peek_front())
# endregion