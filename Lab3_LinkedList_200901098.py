#Syeda Farwa Rizvi- 200901098- BS CS-01 Section A
#linked lists
class node:
  def __init__(self,data=None):#does not make it none if data is provided
    self.data=data
    self.nextPtr=None
    #print("Node is created")#check

class linkedList:
  def __init__(self):
    self.head=node()#create object of node at head
    count=0
    #print("Head is initialized")#check
  #append function
  def insertTail(self,newData):#take new data as argument
    newNode=node(newData)#create new node using new data
    cur=self.head#temp variable
    while (cur.nextPtr!=None):#at the end node add new node
      cur=cur.nextPtr
    cur.nextPtr=newNode

  #insert at head
  def insertFirst(self,newData):
    temp=node()#create node to store current head
    temp.data=self.head.data#store data of current head node in temp
    temp.nextPtr=self.head.nextPtr#" pointer of "
    self.head.data=newData#replace head with new head
    self.head.nextPtr=temp#replace head pointer with temp/prev head
  
  #insert at any point
  def insert(self,after,newData):#take new data to insert, and after which datas node to insert as arguments
    newNode=node(newData)#store new data in a node
    cur=self.head#temp
    while cur.nextPtr!=None:#until end of linked list
       if (cur.data==after):#if the after data is same as current data
         newNode.nextPtr=cur.nextPtr#then insert new node
         cur.nextPtr=newNode
         print("inserted")#check
       cur=cur.nextPtr#next check ptr
  
  #delete end node
  def delete1(self):
    cur=self.head#temp
    while (cur.nextPtr.nextPtr):#when next to next ptr exists:
      secondLastNode=cur.nextPtr#store second last node next ptr(last node ptr)
      cur=cur.nextPtr#store second last as last
    cur.nextPtr=None#in the end remove last pointer by making second last next to null

  #traversal  
  def display(self):#display linked list
     count=0
     cur=self.head
     dis=[]#store linked list in list
     while cur.nextPtr!=None:#until end of list
       cur=cur.nextPtr
       dis.append(cur.data)
       count=count+1#increment size
     print(dis) 
     print("Size of Linked List is ", count)

#CREATING OBJECT AND CALLING
L=linkedList()
L.insertTail(1)
L.insertTail(2)
L.insert(1,5)
L.display()
L.delete1()
L.display()      
