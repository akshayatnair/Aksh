def div(a,b):
    try:
        c = a / b
        print("the result is ", c)
    except:
        print("division by zero error is occured")

x=int(input("enter the first value:\n"))
y=int(input("enter the second value:\n"))
div(x,y)