
a = 25
print(bin(a))
print(oct(a))
print(hex(a))

print("Welcome to python programming")

b = 10
divisible  = 3
if divisible % b == 0:
    print(divisible, "is divisible by", b)
else:
    print(divisible, "is not divisible by", b)

# leap year
year = 2018
if year % 400 == 0:
    print("it is a leap year")
else :
    print("it is not a leap year")

# largest of three numbers
mylist = [2,3,4,5,6,7,8,9,0]
largest = mylist[7]
smallest = mylist[7]
if largest == mylist[7]:
    print(largest,"largest number")
elif largest > mylist[7]:
    print(largest,"largest number")
else:
    print(smallest,"not a largest number")


# student marks 
marks = 35
if marks >= 90:
    print("excellent")
elif marks>=75 and marks<=89:
    print("good")
elif marks>=50 and marks<=74:
    print("Average")
else:
    print("fail")

# right angle triangle
a = 0
while a < 5:
    a+=1
    print('* '*(5-a)+'  '*a)

# prime number 1 to 100
for i in range(2,100):
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count == 2:
        print(i,'prime number')
    else:
        print(i,'not a prime number')

# string
a = "abhilash"
print(a.upper())
print(a.lower())
# print(a.find(2))
# print(a.replace("harish"))
print(a.split)

# count of vowels in string
b = "python programming"
count = 0
for i in b:
    if i in "aeiouAEIOU":
        count+=1
print(count,"number of vowels")

# string is palindrome or not
c = "string"
d = c[::-1]
if c == d:
    print(c,"is palindrome")
else:
    print(c,"is not palindrome")