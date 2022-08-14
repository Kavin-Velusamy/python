###Basic of python

stack
LIFO (last in first out)
methods
push ,pop, peek ,contain
push
size=0
stack.push("a")      # adding one element
size=1.






queue 
FIFO (first in first out)






# int=3534654
# string="any value" (Double arrow mark)
# float=34.44     #decimal value
# List=[" "]      #list inside string
# Tuple=()
#boolean=true,false

#String=Tuple= immutable(we cannot change the value)
#List= mutable 

.
##variable 

# print ("hello world")    # print()- inbulit function
# name="kavin22012004"     # name= variable (we can store the values)  # string ("set of character")-command 
# print("Hi" + name)
# name="john" 
# print ("hi",name )
# price=45
# amount=34.5             #float value
# child = False           #booleam
# print(child)
# print(price)


###string handling

# code="python learning"
# work="'string'"
# name="in github"
# print(work)
    # print(code.upper())         # fully captial letter 
# print(code.lower())         #fully small letter
# print(code.capitalize())    #first letter capital
# print(code.title())         #firat letter and space after the letter is capital
# print(code +" " + name + work)   #connecting the words or numbers
# print(code+" "+name)        #space of the words
# print("python \nlearning")    #this will print in next line
# print("python \t learning") #giving the the double space of the words
# print(code.isupper())        #if all the letter is upper(true)
# print(code.islower())        #if all the letter is lower ()
# print(len(code))             #finding the index of the word
# print(code.find("n"))        #finding the letter (n)
# print(code.count("n"))      #counting the letter (n)
# print(code.replace("a","s")) #replacing the words
# print(code.isalpha())        #finding all the the letter is alpha letter
# print(code.isdigit())
# print(code*5 )              


# ## multiple assignment in single line

# name,age ,weight="kavin",19,52    #types of variable in one line
# print(weight)
# like=dislike=65
# print(dislike) 
# print(like/dislike)
# print(like*dislike)


###Type casting

#otp=3252363
#otp=str(otp)     #type casting
#print("Your otp is" + str(otp))
#print(type(otp))
#count,number=199,"199"
#print(count+1)
# #count="199"
# print(number+"1")

##Assignment 1
# name="Anand"
# leave="15 days"
# year=2021
# print(name,leave,year)

###Assignment 1    #This is correct method
###Dear Anand,
###You have 15 days of Leave Balance for this
###Year(2021)
# name, leave, year ="Anand",15,2021
# print("Dear " + name + ",\nYou have " + str(leave) + " days of Leave Balance for this\nYear("+ str(year)+")")

# name, leave, year ="Anand",15,2021      #### this code is space error beacuse of (,) this  kama
# print("Dear " , name , ",\nYou have " , str(leave) , " days of Leave Balance for this\nYear(", str(year),")")


### Getting the input from the user

# name=input(" Enter your name:")
# print("Hello"+ name)
# height=float(input("Enter the height:"))
# print(type(height))
# height="{:.4f}".format(height/2.54)     ##{} this is for after the float value, 2 digit {:.2},4 digit {:.4}
# print("Your height is "+ str(height) + "cm")
# #print("Your are " + str(height/2.54) + "inches")
# print("Your are " + height + " inches tall")


###Assignment 2
 
# ## Get user input
# ## Name,Email ID and phone number.print the information like this
# ##  ****************************
# ##  UserName: XXXXX
# ##  Email   : XXXXX
# ##  ph      : XXXXX
# ##  ***************************

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")
 
# print("*****************************")

# print("UserName:",Name)
# print("Email :",Email)
# print("Ph :",Phoneno)

# print("*****************************")


# ## This is another type of code 
# ## Assignment 2

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")

# print("*****************************")

# print("UserName :" + Name + "\n   Email :" + Email + "\n      Ph :" + Phoneno )

# print("*****************************")


### Math operation

# a=20
# b=10
# print(a+b , a-b , a*b , a/b , a/50 , b/30 , (a+b)*40 , a+b*30)      ##give output in float (/) division
# print(10/2 , 20*3)
# a=23.5
# print(round(a))      # round is the absolute correct answer
# a=-5
# print(abs(a))        # ABS is the absolute value of a
# a=5
# print(abs(a))
# print(pow(a,4))      # pow is the power of a
# print(a**4)          # this is another mothod of power term
 
# a=55
# b=32
# print(max(a,b))       # maximum value of a,b
# print(min(a,b))       # minimum value of a,b
 
# import math  # math module
# a=45.6
# print(math.ceil(a))
# print(math.floor(a))
# print(math.factorial(9))
# a=6
# print(a%2)
# print(a%5)
# print(a%9)

### Assignment 3

## Get user input 
## Get the number n fron user.compute and print the follwoing values
## 1.log2(n)
## 2.cos(n)
## 3.e**n

print(math.log(16))
print(cos(16))
print(e**16)



