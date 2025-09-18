''' inner and outer functions '''

def outer():
    print("hello")
    def inner():
        print("world")
    inner()
outer()


# program 2

def outer():
    a = 10
    b = 20
    def inner():
        sum = a + b
        print(sum)
    inner()
outer()


# program 3

def outer(a,b):
    print(a,b)
    def inner():
        sum = a + b
        print(sum)
    inner()
outer(10,20)























