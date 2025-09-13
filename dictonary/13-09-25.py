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

why ?

the key values will be change only  if we change key values output will be same 

example :
my_dict = {"d": 1, "e": 2}
for k, v in my_dict.items():
    my_dict[k] = v * v
    print(my_dict)

output :
{'d': 1, 'e': 2}
{'d': 1, 'e': 4}


'''
'''
def add_numbers(a, b, c=0, d=0):
    return a + b + c + d

where we should give any values in parameters we have to assign values in argunments only
and thefore if we seen here c is assigned with value it is an error .

'''

''' 
def test():
    try:
        return 1
    finally:
        return 2
print(test())

output :
2

'''
# section c

''' 
12.	Write a program to implement your own version of the built-in zip() function.
Example:
Input: [1,2,3], ['a','b','c']  
Output: [(1,'a'), (2,'b'), (3,'c')]


'''

'''
program :

def my_zip(list1 ,list2):
    length = min(len(list1),len(list2))
    i = 0
    while i < length:
        return (list1[i],list2[i])
        i+=1
print(list(my_zip([1,2,3],['a','b','c'])))

'''

'''

14.	Write a program to read a file and display the 3 most frequent words along with their counts.

'''













































