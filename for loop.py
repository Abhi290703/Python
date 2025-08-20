# ''' reverse value '''
# for i in range(0,6,1):
#     print(5-i)

# ''' Even and odd number'''
# for i in range(1,2):
#     if i%2 == 0:
#         print("even")
#     else:
#         print("odd")

# ''' factorial '''
# fact = 4
# for i in range(1,5):
#     fact = fact * i
# print(fact)

# ''' fibonacci series'''
# a = 0
# b = 1
# for i in range(0,10):
#     c = a + b
#     a = b
#     b = c
#     print(a,end=' ')


# ''' factorial '''
# fact = 9
# for i in range(1,10):
#     fact = fact * i
# print(fact)

# ''' prime number '''
# pnumber = int(input("enter a number:"))
# count = 1
# for i in range(1,pnumber+1):
#     if pnumber % i == 0:
#         count += 1
# if count == 2:
#     print(pnumber, "is a prime number")
# else:
#     print(pnumber, "is not a prime number")

# ''' 100 prime numbers'''
# for i in range(2,103):
#     count==0
#     for j in range(1,i+1):
#         count+=1
#     if count == 2:
#         print(i,'prime number')
#     else:
#         print(i,'not a prime number')

# ''' matrics '''
# for i  in range(1,5):
#     for j in range(1,4):
#         print(i,'-',j, end=' ')
#     print(' ')

''' prime numbers using for loop '''
for i in range(1,7):
    for j in range(1,7):
        if i>=j:
           print('*',end=' ')
    print(' ')