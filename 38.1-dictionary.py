# DICTIONARY
'''If we want to represent a group of objects as key-value pairs then we 
should go for dictionaries. '''
'''Dictionary in Python is a collection of keys values, used to store data 
values like a map, which, unlike other data types which hold only a 
single value as an element'''
# Characteristics of Dictionary 
# 1. Dictionary will contain data in the form of key, value pairs.
Dict = {1: 'HARSH', 2: 'PRATAP', 3: 'NAYAK'} 
print(Dict) 
# 2. Key and values are separated by a colon “:” symbol 
Dict = {1: 'HARSH', 2: 'PRATAP', 3: 'NAYAK'} 
print(Dict) 
# 3.	One key-value pair can be represented as an item.
dict ={1: "nayak"}
print(dict) 
# 4.	Duplicate keys are not allowed. 
dict ={1:"harsh",1:"harsh"}
print(dict)
# 5.	Duplicate values can be allowed. 
dict ={1:'harsh',2:'harsh'}
print(dict)
# 6.	Heterogeneous objects are allowed for both keys and values. 
dict ={1:100,2:200}
print(dict)
# 7.	Insertion order is not preserved. 
# 8.	Dictionary object having mutable nature. 
dict={1:100,2:200,3:300}
print(dict)
dict[1]=300
print(dict)
# 9.	Dictionary objects are dynamic. 
# 10.	Indexing and slicing concepts are not applicable 
dict={1:100,2:200,3:300}
print(dict)
print(dict[2])
# print(dict[1:2])(error)