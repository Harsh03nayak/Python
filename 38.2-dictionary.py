# Creating an Empty dictionary in Python: 
dict={}
print(dict)
print(type(dict))
# adding items in dictionary
d= {}
d[1]='harsh'
d[2]='pratap'
d[3]='nayak'
print(d)
# accessing dictionary values by using keys
d={1:'harsh',2:'pratap',3:'nayak'}
print(d)
print(d[1])
print(d[2])
print(d[3])
# key error
# print(d[10])
if 10 in d:
    print(d)
else:
    print('key not found')
    
# getting student information's in the form of dictionaries
'''d={}
n=int(input('enter student number:'))
i=1
while i<=n:
    name=input('enter student name:')
    age=input('enter student age:')
    i=i+1
print(d)'''
# updating dictionary element 
# syntex
# d[key]=value
# case 1-
'''while updating the key in dictionary, if the key in not available then 
a new key will be added at the end of the dictionary with the 
specified value'''
d={1:'harsh',2:'pratap',3:'nayak'}
print(d)
d[4]='bhanu'
print(d)
# case 2-
'''if the key is already exists in the dictionary then the old value 
will be replaced with a new value'''
d={1:'harsh',2:'pratap',3:'nayak'}
print(d)
d[2]='kumar'
print(d)
# removing or deleting elements from the dictionary:
# 1.by using the del keyword ,we can remove the keys 
# syntex:- del d[key]
d={1:'harsh',2:'pratap',3:'nayak'}
del d[2]
print(d)

# 2.by using clear() we can clear the objects in the dictionary
# syntex:- d.clear()
d={1:'harsh',2:'pratap',3:'nayak'}
d.clear()
print(d)