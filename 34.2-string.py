# Mathematical operators on string objects in Python 
# We can perform two mathematical operators on a string. Those operators are: 
# 1.	Addition (+) operator. 
# 2.	Multiplication (*) operator. 

'''Addition operator on strings in Python: 
The + operator works like concatenation or joins the strings. 
While using the + operator on the string then compulsory both 
arguments should be string type, otherwise, we will get an error.'''
'''a="harsh"
b="nayak"
print(a+b)
a=str(input("enter first name-"))
b=str(input("enter last name-"))
print(a+" "+b)'''

'''Multiplication operator on Strings in Python: 
This is used for string repetition. While using the * operator 
on the string then the compulsory one argument should be a string and 
other arguments should be int type. '''
'''a="harsh"
b=3
print(a*b)'''

# Length of a string in Python:-- 
'''We can find the length of the string by using the len() function.
By using the len() function we can find groups of characters present 
in a string. The len() function returns int as result. '''
'''name="harsh nayak"
print("the len of the name is-")
print(len(name))'''

# Membership Operators in Python: 
'''We can check, if a string or character is a member/substring of string
or not by using the below operators: 
1.	In 
2.	not in 
in operator:--- in operator returns True, 
if the string or character found in the main string.''' 
'''x="harsh nayak"
print('h' in 'harsh')
print('w' in 'harsh')'''
'''x=input("enter main string")
y=input('enter substring')
if y in x :
    print('substring found in main string')
else:
    print('substring not found in mainstring')'''