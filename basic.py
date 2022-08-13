###Basic of python

# int=3534654
# string="any value" (Double arrow mark)
# float=34.44     #decimal value
# List=[" "]      #list inside string
# Tuple=()
#boolean=true,false

#String=Tuple= immutable(we cannot change the value)
#List= mutable 


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

##Assignment
# name="Anand"
# leave="15 days"
# year=2021
# print(name,leave,year)

###Assignment
###Dear Anand,
###You have 15 days of Leave Balance for this
###Year(2021)
# name, leave, year ="Anand",15,2021
# print("Dear " + name + ",\nYou have " + str(leave) + " days of Leave Balance for this\nYear("+ str(year)+")")



### Getting the input from the user
name=input(" Enter your name:")
print("Hello"+ name)


