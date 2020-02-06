'''def myfunc():
    global x
    x = "fantastic"
myfunc()
print("python is " +x)'''

x = "fantastic"
print("python is " +x)
def myfunc():
    global x 
    x = "awesome"

myfunc()

print("python is " +x)