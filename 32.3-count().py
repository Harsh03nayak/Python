# Count() is a Python built-in function that returns the number of
# times an object appears in a list.
'''list=[10,20,30,40,50]
count=0
for i in list:
    print(i)
    count=count+1
print(count)'''
'''x=eval(input("enter numbers"))
count=0
for i in x:
    print(i)
    count=count+1
print(count)'''

# how count actually work ?
'''x=int(input("enter number for its digit count-"))
count=0
while(x>0):
    y=x%10
    count=count+1
    x=x//10
    print (x)
print(count)'''

# assigning value in variable
x=int(input("enter number for its digit count-"))
y=x
count=0
while(y>0):
    y=x%10
    count=count+1
    y=y//10
    print(y)
print(count)

