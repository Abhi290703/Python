'''
where are some pre-defined methods where we uses rather than the for or loops statemets

iter -> iteration
my_gen -> generators it generates the codes

def __init__ (self):

__init__ is intilization is also called has constructor

object creation :

abhi() -> it is an object


'''

# example program

name = 'AchiversIT'

# this is the complex type

# a = iter(name)
# print(next(a))
# print(next(a))
# print(next(a))

# this is the simplist type to execute

a = iter(name)
for i in name:
    print(next(a))

l1 = [1,2,3,4,5,6,7]
b = iter(l1)
for i in l1:
    print(next(b))


def my_gen():
    yield 1
    yield 2
    yield 3

m = my_gen()
print(next(m))
print(next(m))
print(next(m))

# these are generators it generates the vales without using any loops and iteration


