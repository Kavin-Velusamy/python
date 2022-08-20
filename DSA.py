### DSA in python

# stack
# LIFO (last in first out)
# methods
# push ,pop, peek ,contain

# push
# size=0
# stack.push("a")      # adding one element                     
# size=1                                                        c         third 
#  stack.push("b")      # adding second  element                b       second
# size=2                                                        a    we are adding first element
# stack.push("c")      # adding third element                2323434    this is base element
# size=3 

# pop              # pop means it removes the first element
# size=3
# stack.pop()     # in pop  we added  element
# return =c       # we remove one element ,it returns c
# size=2
# stack.pop()     # in pop  we added second  element
# return =b       # we remove one element ,it returns b
# size-1
# stack.pop()     # in pop  we added three element
# return =a       # we remove one element ,it returns a
# size=0

# peek
# it will not change the element
# size =3
#return c

# contain
# it will find the element 
# stack.contain("c")
# return= true
# stach.contin("d")
# return= false
# size=3

# push and pop

# stack=[]                ##### code
# stack.append(10)      # push
# stack.append(20)
# stack.append(30)
# stack.append(40)
# # print(stack) 
# # stack.pop()        # pop
# # print(stack)
# # stack.pop()
# # print(stack)
# # stack.pop()
# # print(stack)
# # stack.pop()
# # print(stack)
# print(stack[-2])
# print(stack[-1])

# stack=[]              # this stack is empty
# print(len(stack)==0)    # 0 is empty means true
# print(stack)

###Stack using list

# stack=[]
# def push():
##     if len(stack)==n:
##         print("List is full")
##      else:
#         element=input("Enter the element:")
#         stack.append(element)
#         print(stack)
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         e=stack.pop()
#         print("removed element",e)
#         print(stack)
## n=int(input("Enter the limit"))        # this step for limit in stack 
# while True:
#     print("Selected the operation 1.push 2.pop 3.quit")
#     choice=int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         break
#     else:
#         print("Enter the correct operation")

## stack using modules

import collections
stack=collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print(stack) 

## ARRAY 
# ###
# n=int(input("Enter the limit :"))
# a=[]
# print("Enter the number")
# for i in range(n):
#     a.append(input())
# for i in range(n):
#     print("a[",i,"]=",a[i])

###sum of element in array

# n=int(input("Enter the Limit:"))
# a=[]
# sum=0
# print("Enter the element")
# for i in range (n):
#     a.append(int(input()))

# for i in range(n):   
#     sum+=a[i]
# print("sum of array",sum)
    
    
## find
