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

# def leap(a):
#     year = " "
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
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

def list():
    return sum()
num = [1,2,3,7,8]
print("sum",list(num))
