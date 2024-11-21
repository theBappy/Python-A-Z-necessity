astring = "string formatting"
print("single quotes are ' ' ")
print(len(astring))

astirng = "hello world"
print(astirng.index('d'))

astring = 'hello world'
print(astring.count('l'))
print(astring.count('o'))
print(astring.count('r'))

astring = 'hello world'
print(astring[3:7])
print(astring[2:9])
print(astring[4:8])

astring = 'hello world'
print(astring[3:7:2])

astring ='hello world'
print(astring[3:7])
print(astring[3:7:1])

astring = 'hello world'
print(astring[::-1])

astring = 'lieutenant'
print(astring[::-1])

astring = 'Hello World'
print(astring.upper())
print(astring.lower())

astring = 'hello world'
print(astring.startswith('Hi'))
print(astring.endswith('hihihi'))

astring = 'hi how are you'
print(astring.startswith('hi'))
print(astring.endswith('you'))

astring = 'hello world'
print(astring.split(''))

astring = 'hello world'
splitting = astring.split(' ')
print(splitting)

astring = 'hi rebeka how are you'
splitting = astring.split(' ')
print(splitting)

s = 'strings are awesome'
print('lenght of s should be %d' % len(s))
print('the first occurence of in that sentence is a = %d' % s.index('a'))
print('a occurs %d times' % s.count('a'))
print('s occurs %d times' % s.count('s'))
print("the first fives characters are '%s' " % s[:5])
print("the first sevens characters are '%s' " % s[:7])
print("the first nine characters are '%s'" % s[:9])
print("the next fives characters are '%s'" % s[5:10])
print("the thirteenth character is '%s'" % s[12])
print("the characters with odd indexes are '%s'" % s[1::2])
print("the characters with even indexes are'%s'" % s[2::4])
print("The last five characters are '%s'" % s[-5:])
print("the last six characters are '%s'" % s[-6:])
print("the last seven characters are '%s'" % s[-7:])
print("strings in upper case %s" % s.upper())
print("strings in lower case %s" % s.lower())
print("this strings starts with %s" % s.startswith('str'))
print("this strings ends with %s " % s.endswith('nouse'))
if s.startswith('str'):
    print("Strings starts with 'str'.GOOD!")
if s.endswith('some'):
    print("strings ends with 'some'. Great! ")