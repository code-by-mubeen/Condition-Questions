
#1
#Write a program that takes an integer input from the user and prints Even if the number is even and Odd if the number is odd.

num = int(input())      
if num % 2 == 0 : 
    print("Even")       e
else:                   
    print("Odd")        
#------------------------------------

#2
#The user will enter two different integers a and b. Print Greater if a is greater than b. Otherwise print Smaller.

a = int(input())         
b = int(input())            
if a>b :       
    print("Greater")        
else:                       
    print("Smaller")        
#------------------------------------
#3
#Write a program that takes an integer age input from the user. 
#If the age is between 17 and 24 (inclusive), print Ready. Otherwise, print Not Ready

age = int (input())
if (age >=17 ) or (age <=24):
    print("Ready")
else :
    print("Not Ready")

#4
#The user enters a color which can be one of 'green' or 'red'.

    #If the color is 'red', print 'Stop'.
    #If the color is 'green', print 'Go'.
    #Otherwise, print 'Ready'.
#----------------------------------------------------
color = input()            
if color =="red" : 
    print("Stop")        
elif color == "green" : 
    print ("Go")     
else:                        
    print("Ready")         
#------------------------------------
#5
#he user enters an integer score.

    #If the score is greater than 50, print Pass.
    #If the score is less than 50, print Fail.
    #If the score is exactly 50, print Temporary Hold
#-------------------------------------------------

score = int (input())
if score >50 :
 print ("Pass")
elif score <50 :
     print ("fail")
else :
    print ("Temporary Hold")

#----------------------------------
#6
# Write a program that takes two integers and
# an operator ('+', '-', '*', '/') from the user
# and performs the corresponding operation. Print the result.

a = int (input())
b = int (input())
op  = input() 
  

if ( op == "+" ) :
    sum = (a+b)
    print ("a+b =",sum)

elif (op == "-") :
    sub = (a-b)

    print ("a-b = ",sub)
  

elif (op == "*"):

    mul = a*b
    print ("a*b = ",mul)


elif ( op == "/")  :
    div = (a/b)
    print ("a/b = ",div)


else: 
    print ("enter the right operation")

    #dont use detail opertion ("a=b =)
    #---------------------------------------------------------
 
#7 
#Write a program that takes two integers from the user.
# If the first number is between 1 and 10 (inclusive) and the second number is between 20 and 30 (inclusive), print In Range.
#Otherwise, print Out of Range.
#-------------------------------------------------------

a  = int(input())
b  = int(input())
if (a >= 1) == (a <= 10):
    if (b >= 20) == (b <= 30):
        print("In Range")
    else:
        print("In Range")
        
else:

    print("Out of Range")
    #====================================================================
    #8
    #Another way to solve the same problem above is using a single boolean expression:

    a  = int(input())
b  = int(input())
if ((a >= 1) == (a <=10)) and ((b >= 20) == (b <= 30)):
    print("In Range")
else:
    print("Out of Range")
#----------------------------------






















































    
    




































































