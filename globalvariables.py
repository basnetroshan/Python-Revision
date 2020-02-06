#Global variables can be used by everyone both 
# inside and outside the function
# Local variable can be used only inside a function 

x = "awesome" #global variable

def myfunc():
    x = "fantastic" #local variable
    
    print("Python is " +x) #local 

myfunc()

print("Python is " +x) #global

