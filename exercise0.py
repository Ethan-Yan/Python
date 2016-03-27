# Variables
# name = expression

# Strings
# s = '<any string>'

# <string>[<expression>] --> one-character string

s = "Hello"
s[3], s[1 + 1 + 1]
s[0], (s + s)[0]
s[0] + s[1], s[0 + 1]
s[1], (s + 'ity')[1]
s[-1], (s + s)[-1]

# <string>[<expression>:<expression>] --> subsequence

s[0:4]

s[:]
s + s[0:-1+1]
s[0:]
s[:-1]
s[:3] + s[3:]

# <string>.find(<string>)

s.find('llo')

'test'.find('t')
"test".find('st')
"Test".find('te')
'west'.find('test')

s.find(s)
s.find('s')
's'.find('s')
s.find('')
s.find(s + '!!!') + 1

# s = '<any string>'
# t = '<any string>'
# i = <any number>
# s.find(t, i)

s.find('l', 0)
s.find('l', 3)
s.find('l', 4)


# str(<Number>) --> <String>
# x = 3.14159 --> 3; x = 27.63 --> 28

x = 3.14159
# x = 27.63
num = x + 0.5
s = str(num)
point = s.find('.')
print(s[:point])

x = 27.63
