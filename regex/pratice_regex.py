import re as regex

result = regex.match('abc','abcdefg')
print(result)

result = regex.match('abcefg','abcefghijklmonp').group()
print(result)

result = regex.fullmatch('abcefghtiojoi','abcefghtiojoi')
print(result)

result = regex.search('abcdef','abcde')
print(result)

result = regex.findall('asdfghjkl','asdfghl')
print(result)