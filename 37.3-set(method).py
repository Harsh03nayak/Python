# METHOD
# 1. add(only one argument not iterable)
s={10,20,40,50}
s.add(30)
print(s)

# 2.update(iterable obj,iterable obj)
s={10,20,30,40}
s1={50,60,70}
s.update(s1)
print(s)

s2={80,90,100,110,120,130}
s.update(s2,range(3))
print(s)

'''1.	We can use add() to add individual items to the set, whereas we 
can use update() method to add multiple items to the set. 
2.	The add() method can take one argument whereas the update() method 
can take any number of arguments but the only point is all of them 
should be iterable objects. '''

# 3.copy()-clone of set
s={10,20,30,40}
s1=s.copy()
print(s1)

# 4.pop()-This method removes and returns some random element from 
# the set. 
s={1,2,3,4,5,6}
print(s)
print(s.pop())
print(s)

# 5.remove(element)
'''This method removes specific elements from the set. If the specified 
element is not present in the set then we will get KeyError. '''
s={1,2,3,4,5,6}
s.remove(4)
print(s)

# 6.discard(element)
'''This method removes the specified element from the set. If the specified
element is not present in the set, then we won’t get any error. '''
s={1,2,3,4,5,6,7}
s.discard(4)
print(s)

# 7.clear()-removes all element from the set
s={10,20,30}
s.clear()
print(s)