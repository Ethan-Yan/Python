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
