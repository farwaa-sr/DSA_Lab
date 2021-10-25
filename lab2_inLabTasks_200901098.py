#with numpy
import numpy as np
class queue:
  def _init_(self):
    self.list=np.arange(1,2,3,4,5)
  def enqueue(self,data):
    x= np.append(self.list,data)
    return x
  def dequeue(self):
    y=np.delete(self.list,1)
    return y
  def rear(self):
    return self.list[-1]
  def front(self):
    return self.list[0]
  def isEmpty(self):
    return (len(self.list)==0)
  def size(self):
    return (len(self.list)>5)
  def length(self):
    return len(self.list)
def main():
  q=queue()
  q.enqueue(23)
  q.enqueue(34)
  print(q)
  q.deque()
  print(q)

#with collections
from collections import deque
class Queue:
  def __init__(main):
    main.queue=deque([5,2,5,2,6,7])
  def enqueue(main,val):
     a=deque.append(main.queue,val)
     return a
  def dequeue(main):
    b=deque.pop(main.queue,1)
    return b
  def rear(main):
    return main.queue[-1]
  def front(main):
    return main.queue[0]
  def enqueueleft(main):
    c=deque.appendleft(main.queue,val)
    return v
  def dequeueright(main):
    d=deque.popleft(main.queue)
    return d
def main():
  q=Queue()
  q.enqueue(23)
  q.enqueue(34)
  print(q)
  q.deque()
  print(q)
