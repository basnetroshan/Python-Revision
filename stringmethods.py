txt = "i am rosHan"
print(txt.capitalize()) #Capitalises the first letter of the string

txt = "Hello, And Welcome To My World!"
print(txt.casefold()) #Converts string into lower case

txt = "roshan"
print(txt.center(20,'x')) #center align the string, using a specified character (space is default) as the fill character.

txt = "I love apples, apple are my favorite fruit"
x = txt.count("a", 0, 24)
print(x)
