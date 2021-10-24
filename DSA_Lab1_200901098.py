#TASK 1
#Write a Program to check if string entered is palindrome
from collections import deque
string = input("Enter string: ")
stack = deque()
rev = ""#store reverse of string
i = 0
while i < len(string):#while not end of string
    stack.append(string[i])#add string in list
    i = i + 1#increment index
while len(stack) != 0:#while string not empty
    rev = rev + stack.pop()#store reverse of string in rev
if string == rev:#if string and reverse are equal
    print(string, "The string entered is PALINDROME.")
else:
    print(string, "The string entered is not PALINDROME.")

#TASK 2
#Write a program to check the balanced parenthesis in the expression or not using stack
lst=input("Enter:")
stack=[]
dict={'(':')','{':'}','[':']'}
for x in lst:
      if( x == '(' or x == '{' or x == '[' ):
          stack.append(x)
      elif( x == ')' or x == '}' or x == ']' ):
          value = stack.pop()
          if dict[value]!=x :
                print("The Expression is Not Balanced")
      else:
          continue
if not stack:#if stack empty
        print("The Expression is Balanced")
else:
        print("The Expression is Not Balanced")
