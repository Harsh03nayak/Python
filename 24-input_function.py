# In Python, we use the input() function to take input from the user.
# Whatever you enter as input, the input function converts it into a string.
# If you enter an integer value still input() function converts it into a string.
'''name=input("what is your name:")
print("jay shree raam",name,"!")'''
# 1 
'''Taking input from the user'''
'''string=input()
print(string)'''
# 2
'''Convert User Input to a Number'''
'''num=int(input("enter your number:"))
add=num+1
print("the number + 1:",add)'''
# 3
'''Take float input in Python'''
'''takes input from the user in string format converts it into float 
adds 1 to the float,and prints it.'''
'''num=float(input("enter the float number:"))
add=num+1
print("the number + 1=",add)'''
# 4
'''Python Accept List as a input From User'''
'''string=list(input("enter numbers="))
print(string)'''
# 5
'''Take User Input for Tuples and Sets'''
# for tuple
'''string=tuple(input("enter number for tuple formate:"))
print(string)'''
# for set
'''string=set(input("enter number for set formate:"))
print(string)'''
# 6
'''Using input with a dictionary comprehension'''
'''string=("enter a list of words seperated by space:")
words = {word: len(word) for word in str.split()}
print(words)'''
# 7
'''age=input("enter age")
print(type(age))
age=int(age)
print(type(age))
if age>=18:
    print("eligible")
else:
    print("not eligible")'''
# 8 performing operation through input function
'''x=int(input("enter first num :"))
y=int(input("enter second number :"))
z=x+y
print(z)'''