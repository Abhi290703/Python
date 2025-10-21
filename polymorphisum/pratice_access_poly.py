'''
their are three types of access specifiers
1.public
2.private
3.protected
'''

# public
# class example :
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def display(self):
#         print(self.a , self.b)
# r = example()
# r.display()

# private

class example1 :
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self):
        print(self.a , self._b)
w = example1()
w._b = 40
w.display()

# protected

class example2 :
    def __init__(self):
        self.a = 10
        self.__b = 20
    def display(self):
        print(self.a, self.b)
e = example2()
e.display
print(e._example2__b)

