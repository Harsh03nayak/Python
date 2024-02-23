'''Conditional: Statements are executed based on the condition. As shown above in
the flow graph, if the condition is true then one set of statements are executed, and
if false then the other set. Conditional statements are used much in complex
programs.'''
# (complex program)
# There are three types of conditional statements in python. They are as follows:
# 1. if statement
# 2. if-else statement
# 3. nested-if (if-elif-elif-else)
# 1. if statement
'''x=int(input("check eligible or not:-"))
if x>=18:
    print("eligible")'''
# 2. if else statement
# example 1
# "checking weather a number is positive,negative,or zero"
'''x=int(input("enter number:"))
if x<0:
    print("negative")
elif x>0:
    print("positive")
else:
    print("zero")'''
# example 2
# find grater than in x,y,z
'''x=int(input("enter first digit :"))
y=int(input("enter second digit :"))
z=int(input("enter third digit :"))
if x>y:
    if x>z:
        print (x,"is grater")
    else:
        print(z,"is grater")
else:
    if y>z:
        print(y,"is grater")
    else:
        print(z,"is grater")'''
# example 3
# checking if a year is leap year
'''year=int(input("enter year to check leap year"))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("its leap year")
else:
    print("its not leap year")'''
# 3.nested if else
# example 1
# Check your gread based on your own score
'''x=int(input("enter your percentage "))
if x>=90:
    print("a")
else:
    if x>=80:
        print("b")
    else:
        if x>=70:
            print("c")
        else:
            if x>=60:
                print("d")
            else:
                print("f") '''
# Example 2
# Check given year is leep year or not.
'''year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
'''
# 3. if elif else statement in python:
# Example 1-Please choose value within range of o to 4.
print("enter values within range of 0 to 4")
x=int(input("enter the number"))
if x==0:
    print(x)
elif x==1:
    print(x)
elif x==2:
    print(x)
elif x==3:
    print(x)
elif x==4:
    print(x)
else:
    print("beyond the range")

  



