''' inner and outer functions '''

# def outer():
#     print("hello")
#     def inner():
#         print("world")
#     inner()
# outer()


# program 2

'''def outer():
    a = 10
    b = 20
    def inner():
        sum = a + b
        print(sum)
    inner()
outer()'''


# program 3

'''def outer(a,b):
    print(a,b)
    def inner():
        sum = a + b
        print(sum)
    inner()
outer(10,20) '''


''' decorator function :
    decorator function is used for to decorator the function by adding extra function means calling function
    inside the function is called decorator function .
'''

# program 

'''def decorator(a):
    def wrap():
        print('*' * 10)
        a()
        print('*' * 10)
    return wrap()

@decorator
def fun():
    print("hello world")

fun()'''

# lambda function

add = lambda x,y : x+y
print(add(10,20))

import math

print(abs(-12))
print(pow(45,2))
print(round(4.51324,ndigits=3))
print(divmod(50,2))


















