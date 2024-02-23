# A group of characters enclosed within single or double or triple quotes is called a string. 
# We can say the string is a sequential collection of characters. 
# string1="harsh nayak"
# string2='harsh nayak'
# string3='''harsh nayak'''
# print(string1)
# print(string2)
# print(string3)
'''Accessing string characters in python: 
We can access string characters in python by using, 
1.	Indexing 
2.	Slicing '''
# Indexing: 
'''Indexing means a position of string’s characters where it stores. 
We need to use square brackets [] to access the string index. 
String indexing result is string type. String indices should be 
integer otherwise we will get an error. 
We can access the index within the index range otherwise we will get
an error. 
Python supports two types of indexing 
1.	Positive indexing: The position of string characters can be a 
positive index from left to right direction 
(we can say forward direction). In this way, the starting position 
is 0 (zero). 
2.	Negative indexing: The position of string characters can be 
negative indexes from right to left direction 
(we can say backward direction). In this way, the starting position 
is -1 (minus one). '''
'''str1="hello"
print(str1[2])
print(str1[-1])  
print(str1.index('l'))'''
# slicing
'''A substring of a string is called a slice. A slice can represent a 
part of a string from a string or a piece of string. The string slicing
 result is string type. We need to use square brackets [] in slicing. 
In slicing, we will not get any Index out-of-range exception. 
In slicing indices should be integer or None or __index__ method 
otherwise we will get errors. '''
string1="my name is lakhan"
print(string1[::])
print(string1[::-1])
print(string1[::2])
print(string1[-1:-9:-1])
print(string1[-1:-9:-3])
'''Note: If you are not specifying the beginning index, then it will 
consider the beginning of the string. If you are not specifying the 
end index, then it will consider the end of the string. '''
'''Strings are immutable in Python: 
Once we create an object then the state of the existing object
cannot be changed or modified. This behavior is called immutability. 
Once we create an object then the state of the existing object can 
be changed or modified. This behavior is called mutability. A string 
having immutable nature. Once we create a string object then we cannot 
change or modify the existing object. '''
name="harsh nayak"
print(name[0])
name[0]="s" #string is immutable (cannot be changed or modified)

