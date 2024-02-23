# Whenever we want to create a group of objects where we want below
# mention properties, then we are using list sequence. 
# 1.	Duplicates are allowed. 
# 2.	Order is preserved. 
# 3.	Objects are mutable. 
# 4.	Indexing are allowed. 
# 5.	Slicing are allowed. 
# 6.	Represented in square bracket with comma separated objects. 
# 7.	Homogeneous and Heterogeneous both objects are allowed. 1385 h-1338

# duplicates are allowed 
list=[10,20,30,'harsh',10,40,10]
print(list)

# order is preserved 
list=[10,20,30,'harsh',10,40,10]
x=0
for i in list:
    print('list[{}]='.format(x),i)
    x=x+1

# objects are mutable.
list=[10,20,30,'harsh',10,40,10]
x=0
for i in list:
    print('list[{}]='.format(x),i)
    x=x+1
list[3]='nayak'
print(list)

# indexing are allowed  
list=['harsh',10,20,'neeraj',50]
print(list[0])
print(list[-1])

# slicing are allowed
list=['harsh',10,20,'neeraj',50]
print(list[1:4])
print(list[::-1])