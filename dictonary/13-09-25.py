''' 1.	Explain the difference between shallow copy and deep copy with an example program '''

# Shallow Copy :
''' it copies the objects and class shallow copy is independent 
# deep copy :
it copies the objects from the class it is dependent

'''

''' 2.	Why are sets unhashable but frozensets hashable in Python? Give an example use case.'''
# sets unhashable :
''' in sets unhashable type refer to an object where it change it values after it created '''
# fronzensets hashable :
''' it is immutable where it cannot accept an objects and values '''

''' 3. What is the difference between locals() and globals() functions? Demonstrate with a program.'''
# local :
''' in local funtion we have write all code in the function block of code '''
# global :
''' in global function we can write code out of function also global variables can be declared anywhere '''

# program ;
# def greet(a,b):
#     print("sum of",a+b)
# greet(10,20)

# output :
''' sum of 30 '''

''' 4.	Explain how try-except-else-finally works with an example that covers all four blocks. '''
# program 

# def add (x,y):
#     try:
#         result = x//y
#     except ZeroDivisionError:
#         print("sorry | it is zero division error")
#     else:
#         print(result)
#     finally:
#         print("it's true")
# add (10,0)

''' 5. Differentiate between module and package with an example of each.'''
# module :
''' their are some modules how we can write open insert and delete'''
# package :
''' package describe the their some packages like import math , pandas and etc '''



#  Section B 

''' 
6.	Predict the output:

x = [10, 20, [30, 40]]
y = x[:]
y[2][0] = 99
print(x)
print(y)

output :
[10, 20, [99, 40]]
[10, 20, [99, 40]]

'''

''' 
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
print(func(3, []))

output :
[1]
[1, 2]
[3]


'''

'''
    my_dict = {"a": 1, "b": 2}
    for k, v in my_dict.items():
        my_dict[k] = v * v
    print(my_dict)

output :

{'a': 1, 'b': 4}


'''



