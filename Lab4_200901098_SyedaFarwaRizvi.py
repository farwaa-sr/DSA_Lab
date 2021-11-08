#Syeda Farwa Rizvi 200901098 Section A
#Linked List SIngly and Doubly

#TASK 1
class node:
  def __init__(self,data):
    self.data=data
    self.nextPtr=None
class EESportsClub:
  def __init__(self,P,S):
    self.president=node(P)#head
    self.secretary=node(S)#tail
    self.president.nextPtr=self.secretary
    self.secretary.nextPtr=None
    self.count=2
  
  def insert(self,after,newData):#take new data to insert, and after which datas node to insert as arguments
    newNode=node(newData)#store new data in a node
    cur=self.president#temp
    while (cur!=self.secretary):#until end of linked list
       if (cur.data==after):#if the after data is same as current data
         newNode.nextPtr=cur.nextPtr#then insert new node
         cur.nextPtr=newNode
         #print("inserted")#check
       cur=cur.nextPtr#next check ptr
       self.count+=1
    if (cur.data==after):#if the after data is same as current data (for insert after head)
         newNode.nextPtr=cur.nextPtr#then insert new node
         cur.nextPtr=newNode
    elif (after==self.secretary.data):
      temp=self.secretary
      self.secretary=newNode
      self.secretary.nextPtr=None
      temp.nextPtr=self.secretary

  def delete(self,newData): #take node at which deletion is required as argument
    cur=self.president
    prev=cur
    if (newData==self.president.data):
      self.president=self.president.nextPtr
    while (cur.data!=newData and cur.nextPtr!=self.secretary):#until user does not match current data and current is not null node
      prev=cur#temp store prev node
      cur=cur.nextPtr#traverse
    prev.nextPtr=cur.nextPtr.nextPtr#give previous pointer the currents next to next pointer to dereference 
  
  #NODE TRAVERSAL  
  def display(self):#display linked list
     self.count=0
     cur=self.president
     dis=[]#store linked list in list
     while (cur!=self.secretary):#until end of list
       dis.append(cur.data)#append in list node
       cur=cur.nextPtr#traverse
       self.count=self.count+1#increment size
     self.count=self.count+1#increment last node
     dis.append(self.secretary.data)
     print(dis) #display list
     print("Size of Linked List is ", self.count)#display size
  
  def revDisplay(self):
     self.count=0
     cur=self.president
     dis=[]#store linked list in list
     while cur.nextPtr!=self.secretary:#until end of list
       dis.append(cur.data)#append in list node
       cur=cur.nextPtr#traverse
       self.count=self.count+1#increment size
     dis.append(cur.data)#append last node
     self.count=self.count+1#increment last node
     print(dis.reverse()) #display list
     print("Size of Linked List is ", self.count)#display size
#TASk 1 MAIN
pName=input("Please enter President of EE Sports Club's Name: ")
sName=input("Please enter Secratary of EE Sports Club Name: ")
sportsClub=EESportsClub(pName,sName)
c=0
while choice!=5:
 choice=int(input("Enter - '1'. Add the members as well as president or even secretary. '2'. Delete memebers as well as president or event secretary '3'. Compute total number of members of club and display. '4'. Display list in reverse order - store in list and reverse. '5'. Exit"))
 print(choice)
 if (choice==1): 
       data=input("What new element data would you like to enter?")
       after=input("After which data would you want to enter new element")
       sportsClub.insert(after,data)
       sportsClub.display()
 if (choice==2): 
       data=input("What data would you like to delete?")
       sportsClub.delete(data)
       sportsClub.display()
 if (choice==3): 
   sportsClub.display()
 if (choice==4): 
  sportsClub.revDisplay()  
  
 

#TASK 2
class Node:
  def __init__(self,data):
    self.data=data
    self.nextPtr=None
    self.prev=None

#part A
class DlinkedList:
  def __init__(self):
    self.head=None
    self.count=0
#part D
  def insertHead(self, data):#insert node at head
    newNode=Node(data)
    if (self.head==None): #if its empty
     self.head=newNode
    else:
      newNode.nextPtr=self.head
      self.head.nextPtr=None
      self.head.prev=newNode
      self.head=newNode
      self.head.prev=None

  def deleteHead(self):#delete node at head
    if self.head==None:
      print("No Node Exists")
    else:
      self.head=self.head.nextPtr
      self.head.prev=None
#part C
  def insertTail(self,data):
    newNode=Node(data)#create new node using new data
    cur=self.head#temp variable
    if (self.head==None): #if its empty
     self.head=newNode
    while (cur.nextPtr is not None):#at the end node add new node
      cur=cur.nextPtr
    cur.nextPtr=newNode
    newNode.prev=cur
    newNode.nextPtr=None

  def deleteTail(self):
    if self.head==None:
      print("No Node Exists")
    else:
      cur=self.head#temp
      while (cur.nextPtr.nextPtr):#when next to next ptr exists:
       secondLastNode=cur.nextPtr#store second last node next ptr(last node ptr)
       cur=cur.nextPtr#store second last as last
      cur.nextPtr=None#in the end remove last pointer by making second last next to null

#Part B  
  def display(self):#display linked list
     cur=self.head
     dis=[]#store linked list in list
     while (cur.nextPtr): #until end of list
       dis.append(cur.data) #append in list node
       cur=cur.nextPtr #traverse
       self.count=self.count+1 #increment size
     dis.append(cur.data)  #append last node
     self.count=self.count+1 #increment last node
     print(dis) #display list
     print("Size of Linked List is ", self.count) #display size

#TASK 2 MAIN MENU
choice=0
while (choice!=5):#Exit at 5
 print("Welcome. To alter Employee data, Select one of the following: ")
 print("  0. Display Employee Data")
 print("  1. Insert name at Head")
 print("  2. Insert name at Tail")
 print("  3. Remove name at Head")
 print("  4. Remove name at Tail")
 choice=int(input("  5. Exit: "))
 EmployeeData=DlinkedList()
 if (choice==0):
   EmployeeData.display()
 if (choice==1):
   data=input("Enter Employee Name: ")
   EmployeeData.insertHead(data)
 if (choice==2):
   data=input("Enter Employee Name: ")
   EmployeeData.insertTail(data)
 if (choice==3):
   EmployeeData.deleteHead()
 if(choice==4):
   EmployeeData.deleteTail()



