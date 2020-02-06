#Global variables can be used by everyone 
# both inside and outside the function 
x = "awesome"

def myfunc():
    x = "fantastic" #local variable, can be used only inside the function
    print("Python is " +x)

myfunc()

print("Python is " +x)

