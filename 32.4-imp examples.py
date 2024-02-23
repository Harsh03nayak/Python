# O/P-
# *
# **
# ***
# ****
# *****
'''x=int(input("enter the number of rows-"))
for i in range(1,x+1):
    print("*"*i,end="")
    print()'''
#     *
#     **
#    ***
#   ****
#  *****
#  ******
'''x=int(input("enter the number of rows-"))
for i in range(1,x+1):
    print(" "*(x-i),"*"*i,end="")
    print()'''
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5
'''x=int(input("enter the number of rows-"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
'''x=int(input("enter the number of rows-"))
for i in range(x,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''
# *
# ***
# *****
# *******
# *********
'''x=int(input("enter the number of rows-"))
for i in range(1,x+1):
    print(""*(x-1),"*"*(2*i-1))'''