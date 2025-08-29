# name = "Abhi"
# print (name[2])

# # length of string
# print(len(name))   

# # type of string
# print(type(name))

# # directory of string
# print(dir(name))

# # using for loop
# for i in range(0, len(name)):
#     print(name[i])

# # reversing the number
# rev=name[::-1]
# print(rev)

# # by using for loop
# rev = ''
# for i in range (len(name)-2,-1,-1):
#     rev+=name[i]
# if rev == name:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# # to find letter in between

# print(name.find('b'))  # returns index of first occurrence
# print(name.find('d'))
# print(name.find('h',2,3))

# # rfinder 
 
# print(name.rfind('s'))  # returns index of last occurrence
# print(name.rfind('d'))
# print(name.rfind('h',2,6))

#  string methods

# name1 = "achieversIT"

# print(name1.rindex('e',0,10))

# # count 
# print(name1.count('e'))

# #ljust
# subname = name1.ljust(14,"*")
# print(len(subname))
# print(subname)

# #rjust
# subname = name1.rjust(14,"*")
# print(subname)

# #center
# subname = name1.center(25,"*")
# print(subname)

# #z fill
# subname = name1.zfill(20)
# print(subname)

# # count
# subname = name1[0:5].count('e')
# print(subname)

# #l strip
# string = "hello"
# print(len(string))

# #l strip
# string1=string.lstrip
# print(len(string))
# print(string1)

# #r strip
# string1=string.rstrip
# print(len(string))
# print(string1)

# # join and split
# join :
# ex='a-b-c-d-e'
# print(ex.replace('-',','))

# s1 = "Abhi"
# s2 = "nani"
# print(s1.join(s2))

# split
# s3 = "abhilash abhi"
# s4 = s3.split((' '))
# for x in s4:
#     print(x)

# #r split
# s4 = s3.rsplit((' '))
# for x in s4:
#     print(x)

# # splitlines

# para="Hi there is dog"
# print(para.splitlines())

# prefix 
quot="Pyhton is a dynamic language"
# print(quot.startwith("Pyhton"))
# print(quot.endwith('dynamic'))

#remove prefix
# print(quot.removeprefix('Py'))
# print(quot.removeprefix('ht'))

#remove sufix
# print(quot.removesufix('ge'))

#partion
# email='abhi@gmail.com'
# print(email.partition('@'))
# print(email.partition('a'))

#upper
# wish = "hello"
# print(wish.upper)

#lower
# print(wish.lower)

#lower extenstion
greetings = " Hello my friend"
print(greetings.lower())
print(greetings.title())
print(greetings.capitalize())
print(greetings.swapcase())
print(greetings.isalpha())


# isinstance
print(isinstance(79,str))
print(isinstance(79,int))
print(isinstance(79.08,float))
