import re as regex

# result = just.match('abc','abcdefg')
# print(result)

# result = just.match('abc','abcdefg').group()
# print(result)

# by using group() we shows how many values that are matched with each group if not "None".

# result = just.match('abc','defghabc')
# print(result)

# if we given mismatch values it gives "none" and also it checks starting values 


# result = regex.fullmatch('abc','abc')
# print(result)

# result = regex.fullmatch('abcabc','abcabc').span()
# print(result)

# result = regex.fullmatch('abcabc','abcabc').group()
# print(result)


# fullmatch shows that it matches the full values of group if not none

'''
result1 = just.search('can', "i can drive car")
print(result1) 
'''
# it search the same values if not none

'''
result = just.findall('all',"all all the members are in the and all the members of clg all the staff")
print(result)
'''

# it finds all the values if not []

'''
grouping of elements in regex

[0-9a-zA-Z]
[^](not in this group)
^[](staring)
[]{}[](ends with)
r|s
'''

'''
\d(digits (0-9))
\D(non-digits ())
\w(alphanumerics)
\W(nonalphanumeric)
\s(white spaces)
\S(non white spaces)
'''


res = regex.fullmatch(r"\w{3,25}\@(gmail)\.com","abhi1234@gmail.com")
print(res)

# re = just.fullmatch(r"^[A-Z]{1}[a-z]{7}$","Welcome")
# print(re)

# res = just.fullmatch(r'^\w{1}\W\@\d$',"Abhi@123456")
# print(res)


# result = regex.fullmatch("abc","abc").group()
# print(result)