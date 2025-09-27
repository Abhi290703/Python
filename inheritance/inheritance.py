'''
instance : we can access all variables and methods in a class

'''

''' creating a instances variable '''

# class intance:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
        
#     def area(self):
#         return self.l*self.b

#     def rectangle(self):
#         return 2*(self.l*self.b)

# print(intance(20,10).area())
# print(intance(30,30).rectangle())

'''
this method is called instance method 

1. their are some methods class method and variable method

'''

class method :
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def fun(self):
        self.h = 30

    def show(self):
        print(self.l)
        print(self.b)
        print(self.h)
        print(self.c)

r = method(10,20)
r.fun()
r.c=40
r.show()


        


