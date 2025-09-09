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

d3['name'][0] ='puni'
print(d3)




