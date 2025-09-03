''' there are some of the methods in the list

1.append  -> it the adds the values into the list by using this append method it will adds only single values at a time
2.extend  -> it also adds the values into the list by using this extend method it will add multiple values at a time
3.copy    -> it copies the values from one list to another list
4.insert  -> it insert the values into the list

'''

# l1 = [1,2,3,4,5,6,7]

# # append
# l1.append(8)
# print(l1)

# #extend
# l1.extend([9,10,11])
# print(l1)

# #insert
# l1.insert(11,12)
# print(l1)

# #copy
# l2=l1.copy
# print(l2)


# removing elements from the list

'''' 
1.remove
2.pop
3.clear
4.del
'''

# l3 = [1,3,4,5,6,7]

#remove
''' it removes the element from the list which we have given value to it'''

# l3.remove(4)
# print(l3)

# # pop
# l3.pop()
# print(l3)

# # clear
# l3.clear()
# print(l3)

# # del
# del()
# print(l3)

# methods in the list

''' their are some of the methods in the list 
1.index
2.count
3.reverse
4.sort
'''

l4 = [3,4,5,6,7,8,9]

# index 
print(l4.index(8))   # -> here we are giving index values directly in index place

# count
print(l4.count(8))

# reverse
l4.reverse()
print(l4)

# sort
l5 = [10,45,20,39,89,90,56,67,72]
l5.sort()
print(l5)
