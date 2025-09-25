import re as regex
result = regex.match('abc','abcdefg')
print(result)

result = regex.match('abc','abcdefg').group()
print(result)

result = regex.match('abc','defghabc')
print(result)

# if we given mismatch values it gives none and also it checks starting values 

'''
result = regex.fullmatch('abc','abc')
print(result)

result = regex.fullmatch('abcabc','abcabc').span()
print(result)

result = regex.fullmatch('abcabc','abcabc').group()
print(result)
'''

result1 = regex.search('can', "i can drive car")
print(result1)







