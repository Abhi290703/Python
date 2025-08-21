name = "Abhi"
print (name[2])

# length of string
print(len(name))   

# type of string
print(type(name))

# directory of string
print(dir(name))

# using for loop
for i in range(0, len(name)):
    print(name[i])

# reversing the number
rev=name[::-1]
print(rev)

# by using for loop
rev = ''
for i in range (len(name)-2,-1,-1):
    rev+=name[i]
if rev == name:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

# to find letter in between

print(name.find('b'))  # returns index of first occurrence
print(name.find('d'))
print(name.find('h',2,3))

# rfinder 
 
print(name.rfind('s'))  # returns index of last occurrence
print(name.rfind('d'))
print(name.rfind('h',2,6))
