'''
what is list ?
1. list is a collection of elements where it represent '[ ]' brackets 
2. lists are mutable where it accepts all duplictes values
3. list is collection of hetrogenous elements 
4. in lists it converts any data type into list by using list function
5. list is a order collection of elements.
'''

# program

# l1 = [1,2,3,4,5,6,7,8]
# print(l1)

# # to add extra value by using append
''' we can add extra value by using append only we cannot add extra directly'''

# l2 = [1,2,3,4,5,6,7,8]
# l2.append(9)
# print(l2)
'''  append is nothing it adds the value at the end of the list  '''

# # we can print different data-types of values

# l3 = [1,2,3.5,67.9]
# print(l3)

# # list print strings also in the list

# l4 = [1,2,3.5,64.9,"john","don"]
# print(l4)

# # substrings

# l5 = [1,2,3.6,68.9,"john",[2,3,4.5]]

'''representing list index value'''

# print(l5[5][2])
# print(type(l5))  => list
# to see type of list

# different ways to create list

# l6 = list((1,2,3,4,5))
# print(l6)

# l7 = list("string")
# print(l7)

# # creating a empty list
''' will we are using extend it should be represent in the form of tuple or list'''

# l8 = []
# l8.extend([1,2,3,4,5,6,7,8])
# print(l8)

# read and writing a list

# indexing

l9 = [1,2,3,4,5,6,7,8,9]
# print(l9[6])
# print(l9[-6]) 

# l9[0:9]
# print(l9)

# # printing sequences of numbers
# print(l9[::1])

# # printing reverse number
# print(l9[::-1])

# # finding index value
# print(l9[::-1][4])

# # counting numbers from 2 to 5
# print(l9[1:5:1])

# # print negative numbers from the list 
# print(l9[-2:-8:-1])

# indexing and  slicing 
# l9[5]=9
# print(l9)

# adding sub list to it
''' adding sub list after index of 5'''
# l9[5] = [1,2,3,4,5]
# print(l9)

# representing a -ve index
''' here we can see that reverse -4 is the index of the list and 10 is added to list beside of -4 index'''
# l9[-4] = 10
# print(l9)

#  by using boolean value
''' here we are added boolean value it '''
# l9[3] = True
# print(l9)

# adding string to it
''' here we added string to it '''
# l9[2] = "string"
# print(l9)

# adding value to list by using indexes 
''' here we can see that by using double indexs we can insert value to it'''
# l9[1:7] = [10] -> adding value should be represent in the list format
# print(l9)

''' we can add multiple values where it replaces values from given index to last index 
when we given extra index value more it removes that value'''

# l9[0:4] = [13,24,23]
#   | |
#    start index , end index
# print(l9)

# l9[::2] = [99,89,45,56,78,23,34]
# print(l9)

# list concatation and list repeatation

''' list repeatation represents that it repeats the values how many times that we given '''
# l10 = [1,2,3,4]
# l11 = l10 * 3
# print(l11)

''' short circut means : if any one conditon is satsified is called short circut condition'''

# list comprassion 

''' here we can see that in list comprassion it checks the first value if the first value is greater 
than list 2 than list1 will generate list1 is greater if list2 is greater it generates output if in case 
both the lists first value is are less than it checks last value and comapares the both values   '''
l12 = [1,2,3,4]
l13 = [0,6,7,8]

print(l12 < l13)




