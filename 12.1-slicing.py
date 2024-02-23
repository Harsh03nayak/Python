# SLICING IN PYTHON
# SYNTAX- OBJECT[START:STOP:STEP]
# SYNTAX- OBJECT[START:STOP]
'''it enables the users to access the specific range of
elements by mentioning their indices'''
# note- in stop function for positive value (n-1)is used and 
# step cannot be zero
# for negative value (n+1) is used.
# syntex working from left to right (positive indexing)
str=[10,"harsh",30,40,50,60,70,80]
# syntex-(str[start:end{n-1}:step])
print(str[1:3])
# # if not given start point then by default it will start from zero
print(str[:3])
# # if not given end point then by default it will start from start point
print(str[3:])
# # if given step(2,3) then output will be the the numbers jumped
# (default step- 1)
print(str[::2])
# print(str[::-3])
# print(str[-1:3:-1])