''' functions is a method where we can run number time
in functions we can declare any time of data eg : list,arrays,tuples etc
functions creation

def function (name):
// block of code
fun ()

def -> definition
(name) -> parametrs
fun () -> argunments
fun () -> function call // function call means we declare after the block code we declare the fun call
'''

# program 1
''' prime number '''
# def number(n):
#     if n>0:
#         count = 0
#         for i in range(1,n+1):
#             if n%i == 0:
#                 count+=1
#     if count  == 2:
#         print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")

# number(3)


# program 2
''' factorial '''

# def fact(n):
#     fact = 1
#     for i in range (1,n+1):
#         fact=fact*i
#         print(fact)
# fact(3)

# program 3
''' leap year'''

# def leap(year):
#     if (year % 4 == 0 and year % 100 != 0):
#         print("leap year")
#     else :
#         print("not a leap year")
# leap(2021)

# program 4
'''area of square '''

# def square(a,b):
#     print(a*b)
# square(2,4)

# program 5
''' area of cubiod'''

# def cubiod(length,breath,heigth):
#     print(length*breath*heigth,"area of a cubiod")
# cubiod(5,6,heigth=8)
# cubiod(heigth=9,length=5,breath=6)

# program 6
''' list sum '''

# def list(number):
#     return sum(number)
# num = [1,2,3,7,8]
# print("sum",list(num))

# program 7
''' sum of program without using "sum" '''

# number = [10,23,45,67,89]
# def sum(num):
#     total = 0
#     for i in num:
#         total += i
#         return total
# result = sum(number)
# print("total",result)


#  program 8

''' sub program with using sub'''

# number = [3,5,6,7,2,1,2]
# def sub(n):
#     total = 0
#     for i in n:
#         total-=i
#         return total
# result = sub(number)
# print("total", result)

 # program 9
''' sum of programs without using sum'''

# num = [2,6,7,8]
# def add(n):
#     total = 0
#     for i in n:
#         total+=i
#     print(total)
# add(num)

''' subtraction of program without using sub'''

# num = [2,3,4,5,6,7,8]
# def sub(n):
#     total=0
#     for x in n:
#         total-=x
#     print(total)
# sub(num)

''' multi of program without using multi'''



'''div of program without using div'''

''' volume of cubiod '''

# def vol(a,b,c):
#     print(a*b*c)
# vol(2,3,4)


# keyword argunment and position argunment

# position argunment

''' positional argunments are nothing but we have given paticular position for values if we not given
paticular position to values error will occur '''

# def pos(a,b,c):
#     print('sum of pos',a+b+c)
# pos(10,20,30)     '''in this case if we see that i have particula position to values '''

# def pos1(a,b,c):
#     print('sub of numbers',a-b ,b-c,c-a)
# pos1(c=10,b=20,a=30)  
'''in this case if we see that here we have given values to the particular variables so it will occur same value '''

# def pos2(a,b,c):
#     print('sum of pos2',a+b+c)
# pos2(b=20,10,30)    
'''if we see in this case we have given b=20 where we have position to b=20 and remaining values are not assign values to it '''

# num = [2,3,4,5]
# def pos3(a,b,c,d):
#     print(a+b+c+d)
# pos3(*num)

# second method
''' second type directly using sum method '''

# num = [6,7,8,9]
# def pos4(numbers):
#     print(sum(numbers))
# pos4(num)

#  
# def pos(a,b,c):
#     print("sum of pos",a+b+c)
# pos(3,4,a=2)


''' to printing argunments and keyword  '''

# def call(*args):
#     total=0
#     print(args)
# call(1,2,3,4,5,6)

#     for x in args:
#         total+=x
#     print(total)
# call(1,2,3,4,5,6)


''' keyword argunments '''

def key(**kwargs):
    total=0
    print(kwargs)
key(a=10,b=20,c=30)

''' in keyword argunment we cannot give values in the form of for loop'''

''' giving both values in the combining '''

def mat(*args,**kwargs):
    print(args,kwargs)
mat(1,2,3,4,a=6,b=7,c=8,d=9)

# output : (1, 2, 3, 4) {'a': 6, 'b': 7, 'c': 8, 'd': 9}
''' we have given both argunments in the function'''




















