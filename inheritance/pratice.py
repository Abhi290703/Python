class inher :
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def display(self):
            print(self.l , self.b)

w = inher(78,89)
w.display()

# this program is instance variable because we have decalred instance variable " w "

class inher1 :
     def __init__(self,l,b):
          self.l = l
          self.b = b
     def display(self):
        print(self.l + self.b)

inher1(56,89).display()

# this program is class variable because we ahve decalred class variable "inher1" 

          

