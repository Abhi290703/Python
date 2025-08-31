# i = 1  
while True :
    i+=1
    print (i)
    if i<10:
        continue
    else:
        break

# i = 0
while i<10 :
    i+=1
    print (i)
else:
    print("no repetition")

# ''' inreverse rightangle triangle '''
i=9
while i>0 :
    i-=1 # i=i-2
    print("*"*(i+1))    

# ''' in rightangle triangle '''
i=0
while i<9 :
    i+=1
    print(' '*(9-i)+'*'*i)

# second method of rigth angle triangle

j = 0
while j < 7:
    print("*"*j)
    j+=1


# print("************************")


# invert method

j = 6
while j > 1:
    print("*"*j)
    j-=1

# print 1 to 10 numbers


# reverse of 1 to 10 numbers

i = 10
while i>= 0:
    print(i)
    i-=1

# multiplication table

num = int(input("enter a number"))
i = 1
while i <= 12:
    print(num,"x",i,"=",num * i)
    print(i)
    i+=1
   


