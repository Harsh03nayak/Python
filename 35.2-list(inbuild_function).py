# INBUILT FUNCTIONS IN LIST:
# 1.list.append(obj/list/str)- add objects in list
name=['harsh','neeraj','shubham','pandu']
name.append('dharmendra')
print(name)

mobiles=['iphone','samsung','nokia','mi','redmi']
new_mobiles=['poco','realme','nothing']
mobiles.append(new_mobiles)
print(mobiles)

# 2.list.count(obj)-count how many times the given object are present in list
list=[1,2,3,4,5,5,6,7]
count=list.count(5)
print(count)

vowels=['a','e','e','e','i','e','o','e']
count=vowels.count('e')
print(count)

# random
random=["a","b",["a","b"],("a","b"),["a","b"],("a","b"),"a","b"]
count1=random.count("a")
count2=random.count("b")
count3=random.count(("a","b"))
count4=random.count(["a","b"])
print(count1,count2,count3,count4)

# 3.list.extend(list)-add another list in last of the list
list=['harsh','nishit','anshul','arjit','shubham']
list1=['pandu','dharmendra']
list.extend(list1)
print(list)

list=['harsh','shweta']
tuple=('arjit','anshul')
set={'kunal','shubham'}
list.extend(tuple)
list.extend(set)
print(list)

# 4.list.insert(index,obj)-insert given obj in given list
list=[1,2,3,4,5,6,7,8]
list.insert(3,9)
print(list)

list1=['harsh','kush','pranshu']
list1.insert(1,'mansi')
print(list1)
# 5.list.pop(index)-delete last obj from given list
# using index number
list=[1,2,3,4,5,6]
list.pop(1)
list.pop()
print(list)

# 6.list.remove(obj)-remove given obj from given list
# using object
list=[10,20,30,40,50]
list.remove(10)
print(list)

list=['harsh','shubham','pandu']
list.remove('harsh')
print(list)

# 7.list.reverse()-for list in reverse form 
list=[10,20,30,40,50]
list.reverse()
print(list)
#  or
list=[10,20,30,40,50]
print(list[::-1])

# 8.list.sort()-(reverse=True/False) default-False
list=[1,4,2,3,7,6]
list.sort()
print(list)