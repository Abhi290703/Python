
''' reverse value '''
for i in range(0,6,1):
    print(5-i)

''' Even and odd number'''
for i in range(1,2):
    if i%2 == 0:
        print("even")
    else:
        print("odd")

''' factorial '''
fact = 4
for i in range(1,5):
    fact = fact * i
print(fact)

''' fibonacci series'''
a = 0
b = 1
for i in range(0,10):
    c = a + b
    a = b
    b = c
    print(a,end=' ')
