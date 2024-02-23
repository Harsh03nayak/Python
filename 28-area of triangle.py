# to find area of triangle
# formula
# s=(a+b+c)/2
# area =(s*(s-a)*(s-b)*(s-c))**0.5
a=float(input("first side"))
b=float(input("second side"))
c=float(input("third side"))
s=(a+b+c)/2
area =(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of triangle:",area)