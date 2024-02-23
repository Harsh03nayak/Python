'''1. while loop:- The while loop contains an expression/condition. As per the syntax 
colon (:) is mandatory otherwise it throws a syntax error. The condition gives the 
result as bool type, either True or False. The loop keeps on executing the 
statements until the condition becomes False. i.e. With the while loop we can 
execute a set of statements as long as a condition is true.'''
# parts of while loop
# 1.Initialization
# 2.Condition
# 3.Increment/Decrement 
# Example 1-printing numbers from 1-5
'''x=1
while x<=5:
    print(x)
    x=x+1'''
# example 2-(using ",")
'''while x<=5:
    if x<5:
        print(x,end=",")
    else:
        print(x,end="")
    x=x+1'''
# example 3- printing even numbers from 10 to 20
'''x=10
while x>=10 and x<=20:
    print(x)
    x=x+2'''
# example 4- (using',')
'''x=10
while x>=10 and x<=20:
    if x<20:
        print(x,end=",")
    else:
        print(x,end="")
    x=x+2'''
# 5-print 10 neutural number
'''x=1
while x<=10:
    if x<10:
        print(x,end=",")
    else:
        print(x,end="")
    x=x+1'''
# 6-print sum neutral number
'''x=int(input("enter the number"))
sum=0
i=1
while i<=x:
    sum=sum+i
    if i<x:
        print(i,end="+")
    else:
        print(i,end="=")
    i=i+1
print(sum)'''
# 7-even numbers
'''x=int(input("enter number"))
i=1
while i<=x:
    print(2*i)
    i=i+1'''
# 8-using (",")
'''x=int(input("enter the number"))
i=1
while i<=x:
    if i<x:
        print(2*i,end=",")
    else :
        print(2*i,end="")
    i=i+1'''
# 9-using sum
'''x=int(input("enter the number"))
i=1
sum=0
while i<=x:
    if i<x:
        print(2*i,end="+")
    else:
        print(2*i,end="=")
    i=i+1
    sum=sum+i
print(sum)'''
# 10-print odd number
'''x=int(input("enter n odd number"))
i=1
while i<=x:
    if i<x:
        print((2*i-1),end=",")
    else:
        print((2*i-1),end="")
    i=i+1'''
# 11-print the sum of n odd number
x=int(input("enter the n odd number :"))
i=1
sum=0
while i<=x:
    if i<x:
        print((2*i-1),end="+")
    else:
        print((2*i-1),end="=")
    i=i+1
    sum=sum+i
print(sum)