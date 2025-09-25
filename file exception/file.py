
# what is file exception ?

# exception:
# exception occurs in program when an error is occured due to some file missing and etc

# file exception :
# file exception means erros in program but it handles the program

# types of exceptions :
# 1.runtime error
# 2.syntax error
# 3.logical error
# 4.exception handling
# .......etc


# syntax :
# try :
#     code
# exception :
#     code
# else:
#     code
# finally:
#     code


# try :
# it runs the main code inside the try block 

# except :
# you can catch specific errors in the code by throwing if the code

# else :
# it runs the code if the statement if false 

# finally :
# it executes the finally statement 



# program 

# a = int(input("enter a number"))
# b = int(input("enter a number"))

# try :
#     c = a // b
# except :
#     print("error msg")
# else :
#     print(c)
# finally:
#     print("successfully completed")


# program 2


try :
    f = open("data.txt","r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("error msg")
else:
   print(f)
finally :
    print("successfully")

