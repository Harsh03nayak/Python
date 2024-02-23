# 1. upper()
# This method converts all characters into upper case 
str1='my name is harsh nayak'
str2='MY NAME IS HARSH NAYAK'
str3='My Name Is Harsh Nayak'
print(str1.upper())
print(str2.upper())
print(str3.upper())

# 2. lower()
# This method converts all characters into lower case 
str1='my name is harsh nayak'
str2='MY NAME IS HARSH NAYAK'
str3='My Name Is Harsh Nayak'
print(str1.lower())
print(str2.lower())
print(str3.lower())

# 3. Swapcase()
# This method converts all lower-case characters to uppercase
# and all upper-case characters to lowercase 
str1='my name is harsh nayak'
str2='MY NAME IS HARSH NAYAK'
str3='My Name Is Harsh Nayak'
print(str1.swapcase())
print(str2.swapcase())
print(str3.swapcase())

# 4. title()
# This method converts all character to title case 
# (The first character in every word will be in upper case and 
# all remaining characters will be in lower case) 
str1='my name is harsh nayak'
str2='MY NAME IS HARSH NAYAK'
str3='My Name Is Harsh Nayak'
print(str1.title())
print(str2.title())
print(str3.title())

# 5. capitalize()
# Only the first character will be converted to upper case and all
# remaining characters can be converted to lowercase. 
str1='my name is harsh nayak'
str2='MY NAME IS HARSH NAYAK'
str3='My Name Is Harsh Nayak'
print(str1.capitalize())
print(str2.capitalize())
print(str3.capitalize())

#  6. center()
'''Python String center() Method tries to keep the new 
string length equal to the given length value and fills the extra 
characters using the default character (space in this case). '''
# example 1
str1='python program for center()'
str2=str1.center(60)
print(str2)
# example 2
str1='my name is harsh'
str2=str1.center(55,"#")
print(str2)

#  7. count()
# Syntax: string. Count(substring, start= …., end= ….)
'''count() function is an inbuilt function in Python programming language 
that returns the number of occurrences of a substring in the given 
string. '''
str1='my name is harsh nayak'
count=str1.count('a')
print(count)
'''Mandatory parameter:  substring – string whose count is to be found. 
Optional Parameters:  
start (Optional) – starting index within the string where the search starts.
end (Optional) – ending index within the string where the search ends.''' 
str1='my name is harsh nayak'
str2=str1.count('a',1,7)
print(str2)

# 8.join()
'''The string join() method returns a string by joining all the elements of an 
iterable (list, string, tuple), separated by the given separator. ''' 
# join with list
str1=['my','name','is','harsh','nayak']
str2='_'
print(str2.join(str1))
# join with tuples
# example 1
str1=('1','2','3','4')
str2=('+')
print(str2.join(str1))
# example 2
str1=('1','2','3','4')
str2=('abc')
print(str2.join(str1))
# join with sets
str1={'5','4','3','2','1'}
str2=","
print(str2.join(str1))
# join with dictionaries
str1={'my':1,'name':2}
str2='_+'
print(str2.join(str1))

# 9. split()
# The split() method splits a string at the specified separator and
# returns a list of substrings. 
str1="python program to use split function"
print(str1.split(" "))
print(str1.split(" ",2))
print(str1.split(" ",3))