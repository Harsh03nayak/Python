# TUPLE
'''In Python, tuples are immutables.
Meaning, you cannot change items of a tuple once it is assigned. 
There are only two tuple methods count() and index() that a 
tuple object can call. '''
# 1.	Duplicates are allowed. 
tuple=(1,2,3,4,3,2,1)
print(tuple)

# 2.	Order is preserved. 
tuple=(1,2,3,4,5,6,7,8,9)
print(tuple)

# 3.	Objects are immutable. 
tuple=(1,2,3,"harsh",4,5)
# tuple[3]="nayak"
print(tuple)
# syntex error 

# 4.	Indexing is allowed. 
tuple=(1,2,3,4,5,6)
print(tuple[1])

# 5.	Slicing is allowed.
tuple=(1,2,3,4,5,6,7,8)
print(tuple[1:4]) 

# 6.	Represented in parenthesis () with comma separated objects.
tuple=(1,2,3,'harsh','nayak',4,5,6,7) 
print(tuple)

# 7.	Homogeneous and Heterogeneous both objects are allowed.
tuple=(1,2,3,'harsh','nayak',4,5,6,7) 
print(tuple)

# Tuple occupies less memory as compare to list, that’s why tuple 
# is more faster as compare to list.