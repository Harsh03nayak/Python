# example 1
# print the first 10 natural number using for loop.
'''x=int(input("enter the natural number -"))
for i in range(1,x+1):
    if i<x:
        print(i,end=",")
    else:
        print(i,end="")
    i=i+1'''
# in reverse
'''x=int(input("enter n number"))
for i in range(x,0,-1):
    if i<x:
        print(i)
    else:
        print(i)
    i=i+1'''
# example 2
# python program to print all the even numbers 
# method 1 - user gives starting number , and ending number.
'''x=int(input("enter starting number-")) #1
y=int(input("enter ending number-")) #10
i=1
for i in range(x,y+1):
    even=2*i
    if i<y:
        print(even,end=",")
    else :
        print(even,end="")
    i=i+1'''
# method 2 - when last digit is given
'''x=int(input("enter n num-"))
y=int(x/2)
for i in range(1,y+1):
    even=2*i
    if i<y:
        print(even,end=",")
    else:
        print(even,end="")
    i=i+1'''
# O/p-2,4,6,8,10
# in reverse
'''x=int(input("enter starting number-"))
y=int(input("enter stop number-"))
z=int(input("enter step count"))
for i in range(x,y-1,z):
    if i>y:
        print(i,end=",")
    else:
        print(i,end="")
    i=i+1'''
# 10,2,-2
# summing up all even number-
'''x=int(input("enter n number-"))
y=int(x/2)
sum=0
for i in range(1,y+1):
    even=2*i
    if i<y:
        print(even,end=",")
    else:
        print(even,end="")
    sum=sum+even
    i=i+1
print()
print(sum)'''

# example 3
# python program to calculate the sum of all numbers from 1 to
# a given number .
'''x=int(input("last number"))
sum=0
i=1
for i in range(1,x+1):
    if i<x:
        print(i,end="+")
    else:
        print(i,end="=")
    i=i+1
    sum=sum+i
print(sum)'''

# example 4
# python program to print n odd number.
# method 1. when a range is given
'''x=int(input("enter starting number-"))
y=int(input("enter last number-"))
for i in range(x,y+1):
    odd=2*i-1
    if i<y:
        print(odd,end=",")
    else:
        print(odd,end="")
    i=i+1'''

# method 2. when n number is given
'''x=int(input("enter n number-"))
y=int(x/2)
for i in range(1,y+1):
    odd=i*2-1
    if i<y:
        print(odd,end=",")
    else:
        print(odd,end="")'''

# summing up all odd number
'''x=int(input("enter n number-"))
y=int(x/2)
sum=0
i=1
for i in range(1,y+1):
    odd=2*i-1
    if i<y:
        print(odd,end=",")
    else:
        print(odd,end="")
    sum=sum+odd
    i=i+1
print()
print(sum)'''
# in reverse
x=int(input("enter starting number-"))
# y=int(input("enter stop number-"))
# z=int(input("enter step count-"))
for i in range(x,0,-1):
    odd=2*i-1
    if i<x:
        print(odd,end=",")
    else:
        print(odd,end="")
    i=i+1

# example 5
# python program to print a multiplication table of a given number
'''x=int(input("enter number for multiplication table"))
for i in range(1,11):
    print(x,"*",i,"=",x*i)'''
# example 6
# python program to display numbers from a list using a for loop.
'''list=[10,20,30,40,50]
for i  in list:
    print(i)'''
# example 7
# python program to count the total number of digits in a number
'''x=eval(input("enter the numbers-"))
count=0
for i in x:
    print(i)
    count=count+1
print(count)'''