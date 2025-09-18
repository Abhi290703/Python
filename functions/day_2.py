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
























