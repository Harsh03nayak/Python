# BITWISE OPERATOR'S
# bitwise and operator 
# bitwise or  operator
# bitwise not operator
# bitwise zor operator
'''In Python, bitwise operators are used to perform bitwise 
calculations on integers. The integers are first converted 
into binary and then operations are performed on each
bit or corresponding pair of bits,  hence the name bitwise 
operators.The result is then returned in decimal format.'''
# bitwise "and" operator (use &)
# '''sets each bit to one if both bits are one '''
# 0,0-0
# 0,1-0
# 1,0-0
# 1,1-1
a=500
print(bin(a))
a=0b111110100
b=700
print(bin(b))
b=0b1010111100
print(bin(a & b))
print(int(a & b))
