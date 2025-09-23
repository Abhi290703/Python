'''

what is module ?
in python every module is pre-defined
we can import files to another file 

their are 3 ways of import statements

1.import math , pandas , libraries , etc
2.import math as m , math as b , charts as ch
we can define your own names in it
3.we can take a value individually like
from math import pi

'''

# example programs

import math
print(math.pi)


import math as b
print(b.pi)       # here we have given your own variable 

from math import pi
print(pi)


a = 890
b = 567

def sum(a,b):
    print("sum = ",a+b)

def sub(a,b):
    print("rem = ",a-b)

sum(a,b)
sub(a,b)

print("hello welcome")
print(a)
print(b)



