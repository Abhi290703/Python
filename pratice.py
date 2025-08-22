# tuple = ("apple","banana","mango")
# print(tuple)

# list = ["apple","banana","mango"]
# print(list)

# '''string reverse'''
# a = "apple"
# rev = a[::-1]
# print(rev)

# ''' if else statement '''
# if a == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # ''' program 2 '''
# marks = 75
# age = 18
# if marks >= 90:
#     print("A")
#     if age < 18:
#         print("You are eligible for scholarship")
#     elif (marks > 70 and marks < 80):
#         print("B grade")
#         if age >= 21:
#             print("You are not eligible for scholarship")
# else:
#     print("fail")

# ''' program 3 '''
# login = "yes"
# device = "desktop"
# if login == "device":
#     # if device == "mobile":
#         print ("mobile dashboard")
# else:
#         print("desktop dashboard")

# '''program 4'''
# # type conversions

# number = 6
# print(bin(number))
# print(hex(number))
# print(oct(number))
# # print(decimal(number))

# # type conversions 

# print(type(int("10")))  # string to int
# print(int(10.5))  # float to int
# print(int(78))
# print(int(False))

# print(float(24.89))
# print(float(10))
# print(float(False))
# print(float(True))
# print(type(float(23.67)))

# print(bool(1))  # int to bool
# print(bool(23))
# print(type(bool(True)))

# string concatenation
# first_name = 'John'
# last_name = 'srinu'
# full_name = first_name + " " + last_name
# print(full_name)

# even or odd
# a = 8
# if a%2 == 0:
#     print("even")
# else:
#     print("odd")

# # reverse a number
# b = 5
# for i in range(0,5,1):
#     print(5 - i)

# # reverse a string
# c = "abhilash"
# for i in range(-1,5,-1):
#     print(c[i],end='')

# #factorial
# d = 6
# for i in range(1,d+1):
#     d*=i
#     print(d)

#fibonnaci series

# e = 7
# f = 8
# for i in range(0,10):
#     g = e + f
#     e = f
#     f = g
#     print(g)

#prime numbers

# h=int(input("enter a number :"))
# count = 0
# for i in range(1,h+1):
#     if h%i == 0:
#         count+=1
# if count == 2:
#     print(h,'prime number')
# else :
#     print(h,'not a prime number')

# #prime using 2 for loop's

# for i in range(1,20):
#     count = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             count+=1
#     if count == 2:
#         print(i,'prime number')
#     else:
#         print(i,'not a prime number')


# matrix
# for i in range(1,7):
#     for j in range(1,5):
#         print(i," -",j,end = " ")
#     print(' ')


# inveres rigth angle triangle
k = 6
while k>0:
    k-=1
    print('*'*(k-1))

l = 7
while l>0:
    l-=1
    print('?'*(l+1))

#right angle triangle
m = 0
while m<6:
    m+=1
    print(' '*(6-m)+'*'*m)

n = 0
while n<6:
    n+=1
    print(' '*(6-n)+'* '*n)


# no repetation
o = 10
while o > 0 :
    o-=1
    print(o)
else:
    print("no repetation")


# continue and break

p = 11
while True:
    p+=1
    print(p)
    if p == 15:
        break


