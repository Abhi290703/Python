'''
class is an group of properties

object is an instances of a class

here _init_ is a method and also a constructor 
if not we can use either class or static

'''


# class maths :
#     def __init__(self,name,about):
#         self.name=name
#         self.about=about

#     def display(self):
#         print(f'hi hello how are you {self.name} how about {self.about}')

# maths('peter','student').display()



''' by using loops statements'''

# class loops :
#     def __init__(self,n):
#         self.n = n
#     def numbers(self):
#         print("numbers from 1 to",self.n)
#         for i in range(1,self.n+1):
#             print(i)
# m = loops(10)
# m.numbers()



''' while loop '''
''' smaller'''

# class whileloop :
#     def __init__(self,n):
#         self.n = n
#     def numbers (self):
       
#         num = self.n
#         while num < 78:
#             print(num)
#             num+=10
        
# obj=whileloop(5)
# obj.numbers()



''' greater numbers'''

# class whileloop :
#     def __init__(self,n):
#         self.n = n
#     def numbers (self):
       
#         num = self.n
#         while num > 0:
#             print(num)
#             num-=1
        
# obj=whileloop(10)
# obj.numbers()


''' multiplication using for loop '''

# class loop :
#     def __init__(self,n):
#         self.n = n
#     def mult(self):
#         print("multiplication of table {self.n}")
#         for i in range(1,self.n+1):
#             print(f" {self.n} * {i} = {self.n * i}")
# obj = loop(13)
# obj.mult()
    

''' by using class '''

# class classs:
#     def data(self,name,age):
#         self.name="Abhi"
#         self.age=22
#     def display(self):
#         print("Name", self.name, "age", self.age)

# s1 = classs()
# s1.data("Abhi",22)
# s1.display()


''' by static '''

class static:
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def square(x,y):
        return x * y
print("Addition:",static.add(4,9))
print("Square:",static.square(8,8))

