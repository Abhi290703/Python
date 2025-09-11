''' 
what is dictonary ?
dictonary is nothing but it have both key and value pairs where we enter the key value in the braces
dictonary is mutable we can write any datatype in it.

'''

# program 1
d1={'one':1,'two':2,'three':3,'four':4}
print(d1)

# 2 method
''' in dictonary we can elements in both list and dictonary format '''
d2 = [{'one':1},{'two':2},{'three':3},{'four':4}]
print(d2)

# 3 method
''' in dictonary we can write both tuple list and also list set '''

d3 = {'name':('nuni','nani','boni'),'age':(21,22,23),'loc':('hyd','bachu','jntu')}
# print(d3)

''' to only index value'''

for i in d3['name']:
    print(i)

for i in d3['age']:
    print(i)

''' we can modify the value i it '''

# d3['name'][0] ='puni'
# print(d3)

# zip function

l1 = [1,2,3,4]
l2 = ['one','two','three']
l3 = dict(zip(l1,l2))
print(l3)

''' if there is no dict keyword o/p will not be generated '''

# undefined value

l4 = [1,2,3,4,5]
l5 = ['one','two','three','four']
l6 = dict(zip(l4,l5))
print(l6)

''' has we seen here we have given undefined value where output was not generated for it was generated 
upto defined value.
'''

# enumarted value

l6 = dict(enumerate(l5))
print(l6)

l6 = dict(enumerate(l5,start=1000))
print(l6)

l5 = dict(enumerate(l5,start=20002201))
print(l5)

''' comprehension with iterable pairs'''

l7 = {x:y for x,y in l4}
print(l7)

