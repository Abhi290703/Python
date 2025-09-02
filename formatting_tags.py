# to find the order of the alphabets 

value = "A"
print(ord(value))

# c style printing
# it is a 32gb hard drive coast about 21.90

memory = 32
device = "hardware"
price = 21.90
# print('it is a',memory,'gb',device,'cost about',price)
# print('it is a %dgb %s cost about $%f'%(memory,device,price))
# print('it is a',device, memory, 'gb cost about', price )
# print('it is a %d gb %s cost about $%f'%(device,price,memory))


# space conviction
print('it is a {}gb {} cost about ${}'. format(memory,device,price))
print('it is a {}gb {} cost about ${}'. format(device,memory,price))
print('it is a {1}gb {0} cost about ${2}'. format(device,memory,price))

print(f'it is a {memory}gb {device} cost about ${price}')
