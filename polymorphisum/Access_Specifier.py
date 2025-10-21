class example :
    def __init__(self):
        self.a = 10
        self.b = 20

    def display (self):
            print(self.a,self.b)

w = example()
w.display()

# code in public mode

# private

class example1 :
    def __init__(self):
        self.a = 10
        self.b = 20

    def display (self):
            print(self.a,self._b)

n = example1()
n._b=30
n.display()

# private

class example1 :
    def __init__(self):
        self.a = 10
        self.__b = 20

    def display (self):
            print(self.a,self.__b)

m = example1()
m.display()
print(m._example1__b)