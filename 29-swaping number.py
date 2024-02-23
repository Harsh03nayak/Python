# python program to swap two numbers
# without using third veriable
'''x=input("enter value of x: ")
y=input("enter value of y: ")
x,y=y,x
print(x)
print(y)'''
# by using third veriable
'''x=input("enter value of x: ")
y=input("enter value of y: ")
z=x
x=y
y=z
print(x)
print(y)'''
# by using addition and subtraction
'''x=int(input("enter value of x: "))
y=int(input("enter value of y: "))
x=x+y
y=x-y
x=x-y
print(x)
print(y)'''
# by using multiplication and division
'''x=int(input("enter value of x: "))
y=int(input("enter value of y: "))
x=x*y
y=x/y
x=x/y
print(x)
print(y)'''
# by using xor veriable
x=int(input("enter value of x: "))
y=int(input("enter value of y: "))
x=x^y
y=x^y
x=x^y
print(x)
print(y)