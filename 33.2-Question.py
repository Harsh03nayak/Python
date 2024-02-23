# Example 8
# python program to check if the given number is palindrome
'''x=str(input("enter number to check palindrome-"))
y=x[::-1]
if y==x:
    print(y,"number is palindrome")
else:
    print(x,"number is not palindrome")'''

# Example 9
# python program that accepts a word from user and reverses it
'''x=str(input("enter a word to reverse it-"))
y=x[::-1]
print(y)'''

# Example 10
# python program to check if the given number is armstrong or not
'''x=int(input("enter number to check armstong or not-"))#took number
y=x #using value for second loop
z=y
sum=0 #finding sum
count=0 #finding count
while(x>0): #for loop break with the digit count
    x=x//10 #for eleminating last digit
    count=count+1 #counting
print(count) #output count
while(y>0): #for loop break with sum of power(digit) with each digit
    mod=y%10 #for using only last digit
    expo=mod**count #last digit **(count)
    sum=sum+expo #
    y=y//10
if(z==sum):
    print(sum,"Number is armstrong")
else:
    print(x,"Number is not armstrong")'''

# example 11
# python program to count the number of even and odd numbers from 
# a series of numbers
'''x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    if i%2==0:
        print(i,"number is even")
    else:
        print(i,"number is odd")'''

# python program to count the number of even and odd numbers from 
# a series of numbers taking from user
# using split
'''x=input("enter series of numbers-")
y=x.split()
i=1
for i in y:
    i=int(i)
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
    i=i+1'''

'''# python program to print prime numbers
x=int(input("enter starting number-"))
y=int(input("enter ending number-"))
print("prime number between",x,"and",y,"are")
i=0
for num in range(x,y+1):
    if i>1:
        for i in range(2,num):
            if num % i==0:
                break
            else:
                print(i)
# example 12- python program to display all numbers withih a 
# range except prime numbers
x=int(input("enter starting number-"))
y=int(input("enter stop number-"))
# z=int(input("enter step number-"))
i=0
for i in range(x,y+1):
    print()'''

lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)