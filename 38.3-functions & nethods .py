# 1.dict()function-d=dict()
# this is used to create an empty dictionary 
d=dict()
print(d)
print(type)
# 2.len()-len(d)
# this function returns the number of items in the dictionary
d={1:'harsh',2:'pratap',3:'nayak'}
print(len(d))
# 3.clear()-d.clear()
d={1:'harsh',2:'pratap',3:'nayak'}
d.clear()
print(d)
# 4. get () d.get()
'''this method used to get the value associated with the key. This 
is another way to get the values of the dictionary based on the key
the biggest advantage it gives over the normal way of accessing a 
dictionary is, this doesn't give any error if the key is not present
'''
# case 1:-
'''if the key is available, then it returns the corresponding value
otherwise return none. it won't raise any error'''
d={1:'harsh',2:'pratap',3:'nayak'}
print(d.get(1))
print(d.get(2))
print(d.get(3))
print(d.get(4))
# case 2:-
'''if the key is available, then returns the corresponding value 
otherwise returns the default value that we give '''
# syntex:-d.get(key,defaultvalue)
d={1:'harsh',2:'pratap',3:'nayak'}
print(d.get(1,'nayak'))
print(d.get(3,'pratap'))
print(d.get(4,'bhai'))
# 5:-pop():-d.pop(key)
'''this method removes the entry associated with the specified 
key and returns the corresponding value. if the specified key is 
not available, then we will get keyerror  '''
d={1:'harsh',2:'pratap',3:'nayak'}
d.pop(2)
# d.pop(5) key error 
print(d)
# 6.popitem() method 
d={1:'harsh',2:'pratap',3:'nayak'}
d.popitem()
print(d)
# 7.keys () 
'''method this method returns all keys associated with the 
dictionary''' 
d={1:'harsh',2:'pratap',3:'nayak'}
print(d.keys())
for i in d.keys() :
    print(i)
# 8.value() method:
'''this method return all the values associated with the
dictionary'''
d={1:'harsh',2:'pratap',3:'nayak'}
for i in d.values():
    print(i)
# 9. item () method:
'''a key value pair in a dictionary is called an item.
item() method returns the list of tuples representing key 
value pairs '''
d={1:'harsh',2:'pratap',3:'nayak'}
for k in d.items():
    print(k)