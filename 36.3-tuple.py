# method
# 1. Count(obj). (How many occurrences)  
tuple=(1,2,3,(1,2),('harsh'),(1,2),1,3,[1,2],[1,2])
count1=tuple.count(1)
count2=tuple.count((1,2))
count3=tuple.count([1,2])
count4=tuple.count(('harsh'))
count5=tuple.count('harsh')
print(count5)

# 2. Index(obj,start,stop)(obj is compulsory argument but rest 
# are optional) 
tuple=(1,2,3,4,5,3,6,7,8)
index=tuple.index(3)
print(index)

tuple=(1,2,3,4,5,3,6,7,8)
index=tuple.index(3,3,7)
print(index)