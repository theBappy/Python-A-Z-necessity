# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))
# print(help(camelcase))


# import re

# txt = "The rain in Spain"

# x = re.search(r"\bS\w+", txt)
# print(x.span())
# print(x.string)
# print(x.group())

# x = re.split('\s', txt, 2)
# u =re.sub("\s", "9", txt, 2)
# print(u)
# print(x)

# x = re.search("Portugal", txt)
# print(x)


# x = re.findall("portugal", txt)
# print(x)
               


'''
[] = set of charactes "[a-m]
\ = signals a special sequence \d \t \n
. = any character "he..o"
^ = starts with "^hello"
$ = ends with "rain$"
* = zero or more occurences
+ = one or more occurences
? = zero or one occurences
{} = exactly the specified the number of occurences
| = either or
() = capture a group
\A = returns a match if the speicifed characters are a the beginning of the string
\b = returns a mathc where the sepcified characters are at the beginning or the the end of a word
\B = where specified characters are presend, but not at the beginning 
\d = string contains digits
\D = does not contains digits
\s = contains white space
\S = no white space
\w = any word
\W = does not contain any words
\Z = at the end of the string
[arn] = a, r, n present 
[a-n] = a to n
[^arn] = match for any characters except a,r,n
[0123] = digits
[0-9] = 0 to 9
[0-5][0-9] = 00 and 59
[a-zA-Z] = lower to upper all
[+] = returns a match for any + character in the string


'''
# txt = "hello planet"

# a = re.findall("he.{2}o", txt)
# print(a)

# z = re.findall("he.?o", txt)
# print(z)

# y = re.findall("he.+o", txt)
# print(y)

# x = re.findall("he.*o", txt)
# print(x)


# x = re.search('Spain$', txt)
# print(x)


# x = re.findall("^The", txt)
# print(x)



# x = re.findall("[a-m]", txt)
# y = re.findall("\d", txt)
# print(y)
# print(x)


# x = re.search("^The.*Spain$", txt)
# print(x)