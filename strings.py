a = "Double Hello" #double quote
b = 'Single Hello' #single quote
print(a)
print(b)

#Multi line String in double quote
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(c)

#Multi line String in single quote
d= '''\nLorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(d)

#String is the array of unicode character
e = "Hello, Roshan"
print(e[1]) #returns value of 1 position

#slicing
print(e[2:8])#returns value of position from 2 to 8(not included)

#Negative indexing
print (e[-5:-2]) #returns value from position 5 to 2, count starting from end of string

print(len(e)) #returns the length of the string

#Strip
p = " HELLO ROSHAN "
print(p.strip()) #returns "HELLO ROSHAN", removes whitespace from the start and end of the string

#lower
q=print(p.lower())

#upper
q = 'hello there'
print(q.upper())

#replace
r = "Yeh Yu-Yun"
print(r.replace('-', 'R')) #replaces the string with another string

#split
print(r.split('-')) #splits the string if it finds the instances of the seperator

#Check String
txt = 'Nepal has an estimated population of 26.4 million'
chk = 'mill' in txt #check if the phrase is in the given string
chk1 = 'lapeN' in txt
chk3 = 'mill' not in txt 
chk4 = 'lapeN' not in txt
print (chk)
print(chk1)
print(chk3)#returns False
print(chk4)#returns True

#Concatenation using + operator
first = "Roshan"
last = "Basnet"
full_name = first + " " + last
print(full_name)