'''The Python range function helps to generate a sequence of numbers. Or this 
Python range function helps to iterate items in iterables such as Lists, Tuples, Sets, 
Strings, etc.'''
'''The syntax of this Python function contains range start, stop, step. All the 
arguments such as start, stop, and step accepts positive or Negative integers.
Syntax: range(start, stop, step)
# Start(optional) - Starting position number. If you omit this, the Python range 
function will start from 0.
# Stop - A value before this number is the end value. For example, (1, 10) 
print values from 1 to 9.
#  Step (optional) - Sequence of numbers generated. It determines the space or 
difference between each integer value. For example, (1, 10, 2) returns 1, 3, 
5, 7, and 9. You can notice that the difference between each integer is 2.'''
# Python's built-in range() function is mainly used when working with for loops –
# you can use it to loop through certain blocks of code a specified number of times. 
# The range() function accepts three arguments – one is required, and two are 
# optional. By default, the syntax for the range() function looks similar to the 
# following:
'''range(start, stop, step)'''
# x=range(10)
# x=range(1,11)
'''x=range(4,20,2)
print(x)
print(list(x))
print(set(x))
print(tuple(x))'''
# transfer statement
# 1. break
# 2. continue
# 3. pass
# break statement-
''' We can use break statement inside loops to break loop 
execution based on some condition.'''
'''for i in range(10):
    if i==7:
        print("done")
        break
    print(i)'''

'''list=[10,20,30,40,50]
for i in list:
    if i>40:
        print("i is greater than 40")
        break
    print(i)'''
# continue
'''We can use continue statement to skip current iteration and 
continue next iteration.'''
'''list=[10,20,30,40,50,20,10]
for i in list:
    if i>45:
        print("done")
        continue
    print(i)'''
# pass
'''pass is a keyword in Python. In our programming syntactically if block is required 
which won't do anything then we can define that empty block with pass keyword.'''
# 1. It is an empty statement
# 2. It is null statement
# 3. It won't do anything
'''for i in range(100):
    if i%9==0:
        print(i)
    else:
        pass'''