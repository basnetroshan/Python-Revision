'''Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview '''

#Getting data type
x = 5
print(type(x))

x = "Hello World"
print(type(x))

x = 20.5
print(type(x))

x = 1j	
print(type(x))

x = ["apple", "banana", "cherry"]	
print(type(x))

x = ("apple", "banana", "cherry")	
print(type(x))

x = range(6)	
print(type(x))

x = {"name" : "John", "age" : 36}	
print(type(x))

x = {"apple", "banana", "cherry"}	
print(type(x))

x = frozenset({"apple", "banana", "cherry"})	
print(type(x))

x = True	
print(type(x))

x = b"Hello"	
print(type(x))

x = bytearray(5)	
print(type(x))

x = memoryview(bytes(5))	
print(type(x))

x = str(20) #setting the specific data type
print(type(x))