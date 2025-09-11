''' 
we are representing values
1.keys
2.values
3.set
4.get
'''

''' obtaining keys '''

d1 = {1:"one",2:"two",3:"three",4:"four",5:"five"}
# a = d1.keys()
# print(a)

# for x in a:
#     print(d1[x])

''' obtainig values '''

# b = d1.values()
# print(b)

# for x in b:
#     print(x)

info = {"name":"Abhi","age":22,"loc":"eluru"}
# Person = info.keys()
# print(Person)

# Person = info.values()
# print(Person)

# for x in Person:
#     print(x)

# # items
# items = info.items()
# print(items)

# #  get method

# g = info.get("name")
# print(g)

# ''' if we given missing value which is not their '''
# g = info.get('job')     # here we have given job which is not in the dictonary output will be none
# print(g)

# # set default

# s = info.setdefault("loc") # we have write set default keyword if we write set it does not recoginces it
# print(s)

# s = info.setdefault("job")   # here also same thing happen when we given missing value
# print(s)

# update
infou = {'degree':'B.tech','college':'GEC','Passout':2025}
info.update(infou)
print(info)

#  copy

d2=d1.copy()
print(d2)

# pop
d2.pop(5)
print(d2)

# popitem
d2.popitem()
print(d2)

# clear
d2.clear()
print(d2)
