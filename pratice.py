# if-else statement program

# a = 20
# b = 0
# if (a < b):
#     print("largest number")
# else :
#     print("smallest number")

# even and odd number

# c = 12
# num = 0
# if(num % 2 == 0):
#     print("even number")
# else:
#     print("odd number")

# if statement

# d  = 10
# e = 10
# if(e == d):
#     print("my number")
# else :
    # print("your number")

# else if statement

# marks = int(input("enter a number"))

# if marks >=90:
#     print("A+ grade")
# elif marks >= 75 and marks <= 89:
#         print("A grade")
# elif marks >= 55 and marks <= 74:
#         print("B grade")
# elif marks >= 45 and marks <= 54:
#         print("D grade")
# else:
#     print("Fail")

# checking whether condition the given number is positive or negative

# f = 0
# if(f > 0):
#     print("positive number")
# elif f < 0:
#     print("negative number")
# else:
#     print("zero")


# age category

# age = int(input("enter a age"))

# if age < 13:
#     print("child")
# elif age >= 18 and age <= 20 :
#     print("youth")
# elif age >= 21 and age <= 29:
#     print("teenage")
# elif age >= 30 and age <= 59:
#     print("gentleman")
# else:
#     if age > 60:
#         print("senior citizen")
#     else:
#         print("not a senior citizen")

# determine if the number is +,-,0

# num = 11
# if num == 0:
#     print("zero")
# elif num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# leap year program

# year = int(input("enter year"))

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("leap year")
# else :
#     print("not a leap year")

# how to write remainder
# number = 56789
# while number > 0:
#     r = number%5
#     print(r)
#     number//=5

# reverse a number using while
# anumber = 7227
# act = anumber
# rev = 0
# while anumber > 0:
#     r = anumber%10
#     rev = rev*10+r
#     anumber//=10
#     print(rev)
# if act == rev:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# rigth angle triangle

# g  = 0
# while g < 7:
#     g+=1
#     print(" "*(7-g)+"*"*g)

# # invert right triangle

# h = 7
# while h > 0:
#     h-=1
#     print("*"*(h))

# second type

# i = 0
# while i < 6:
#     print("* "*i)
#     i+=1

# invert type

# j = 5
# while j > 0:
#     print("* "*j)
#     j-=1



# for loops

# factorial number

# prime number

# n = int(input("enter a prime number : "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count+=1
# if count == 2:
#     print(n,"it is a prime number")
# else:
#     print(n,"it is not a prime number")

# second method

# for i in range (2,50):
#     count = 0
#     for j in range (1,i+1):
#         if i%j == 0:
#             count+=1
#     if count == 2:
#         print(i,"it is a prime number")
#     else:
#         print(i,"it is not a prime number")


# console.log("*****************************")

# multiplication 
# a = 4
# i = 1
# while i <= 12:
#     print(a,"X",i,"=",a * i)
#     i+=1



# operations 

# Assignment operator

# a = 10
# b = 20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)

# # relational operator

# a = 5
# b = 4
# print(a+b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a!=b)
# print(a==b)


# arthimatic operator

# a = 5

# a+=3
# print(a)
# a-=4
# print(a)
# a*=5
# print(a)
# a/=6
# print(a)
# a%=3
# print(a)


# logical operator



# conditional statements

''' 
in conditional statements their are 4 types 
1.if
2.if - else
3.else if
4.nested if
5.switch case

'''

# if-else statement

# problem 1

# city = "eluru"
# if city == "eluru":
#     print(city,"reached")
# else:
#     print(city,"reached vijayawada")

#  problem 2

# items = "none"                      # variable declaration
# if items == "soaps":                #  condition if items are true
#     print(items,"i have taken")         # it prints items if not does not prints
# else:
#     print("just visit and come")

# problem 3

# num = 12

# if num % 3 == 0:
#     print("Divisible by 3")
# elif num % 4 == 0:
#     print("Divisible by 4")


''' dictonary '''

# d1 = {1:'one',2:'two',3:'three',4:'four',5:'five'}
# a = d1.keys()
# print(a)

# b = d1.values()
# print(b)

# for x in a:
#     print(x)

# for x in b:
#     print(x)

#  methods

# items

# info = {"name":"Abhi","age":22,"loction":"eluru","qlf":"B.tech"}
# # a = info.items()
# # print(a)

# # update
# infos = {"desgi":"study","pres-loc":"kphb"}
# info.update(infos)
# print(info)

# # get 
# c = info.get("pres-loc")
# print(c)

# # setdefault
# d = info.setdefault("desgi")
# print(d)

# # pop
# info.pop("pres-loc")
# print(info)

# # popitem
# # info.popitem("desgi")
# # print(info)

# # clear
# info.clear()
# print(info)

# _________________________________________________________________________________________________________


''' 
1.what is python ?
python is high-level programming language 
where python is a interpreted language where each and every line code will be executed before
turning into machine code

2.why python is hybrid language ?
python is hybrid language because first it compiles into byte code and then it interpets bytecode at 
runtime.

3.Their are 3 types of centeric
    1.functional
    2.data
    3.module

4.Datatypes in python
    1.Numeric
        a.int
        b.float
        c.boolean
        d.complex
    
    2.Sequentical
        a.list
        b.tuple
        c.string
        d.array
        e.bytearray

    3.sets
        a.set

    4.dist
        a.dictonary

How many types of converstions are their ?
1.implict conversition
2.explict converstion

Implict Converstion :
1.int
2.float
3.complex
4.boolean

Explict Converstion :
1.tuple
2.list
3.string
4.array
5.bytearray

what are primitive data type and non-primitive data type

primitive data type :
int
float
boolean
string
complex

Non-primitive data type:
list
tuple
sets
dictonary
array



'''

# programs

''' if statements '''

# a = 10
# if a == 10:
#     print(a)

# b = "abhi"
# if b != "abhi":
#     print("none")
# else:
#     print("correct")

''' 3. WAP to display the last digit of a number '''

# num = int(input("enter a number"))
# if num < 10:
#     print(num)
# else:
#     last = num % 10
#     print(last)

''' 4. WAP to check if a number is even or odd where the number is taken as input. '''

# num = int(input("enter a number"))
# if num%2 == 0:
#     print(num,"even number")
# else:
#     print(num,"odd number")

''' 5. Check if the first and last number of a list is same or not. '''
# c = (1,2,3,4,5,6,7,8,9,1)
# if c[0] == c[9]:
#     print("both are equal numbers")
# else:
#     print("both are not equal numbers")

''' 6.WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user. '''

t = int(input("enter marks"))
h = int(input("enter marks"))
e = int(input("enter marks"))
m = int(input("enter marks"))
s = int(input("enter marks"))

total_marks = int(input("enter highest marks"))
sub_marks = t+h+e+m+s
perc = (sub_marks/total_marks)*100

if perc > 90:
    print("A+")
elif perc > 78 and perc < 90:
    print("B+")
elif perc > 68 and perc < 77:
    print("c+")
elif perc > 58 and perc < 68:
    print("D+")
else :
    print("fail")











