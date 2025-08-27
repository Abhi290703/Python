# prime numbers
# n = int(input("enter a prime number :"))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count+=1
# if count == 2:
#     print(n,"it is a prime number")
# else:
#     print(n,"it is not a prime number")


# factorial number

# n = int(input("enter a factorial :"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
#     print(fact)

# 1 to 100 prime numbers
# for i in range (2,103):
#     count = 0
#     for j in range (1,i+1):
#         if i%j == 0:
#             count+=1
#     if count == 2:
#         print(i,"it is a prime number")
#     else:
#         print(i,"it is not a prime number")


# matrics
# for i in range (1,5):
#     for j in range(1,4):
#         print(i,'-',j,end = " ")
#     print(' ')

# right angle triangle 
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*', end =" ")
    print(" ")


# invert right angle triangle
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print('*', end = " ")
    print(" ")



