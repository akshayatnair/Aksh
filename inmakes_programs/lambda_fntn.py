#def addition(a):
   # return(a+10)
#print(addition(5))

 #q=lambda a:a+10
#print(q(5))
#q=lambda a,b,c,d:a+b+c*d+a
#print(q(2,8,9,6))

def sample(x):
    return lambda a:a+x
anw=sample(2)

anw2=sample(7)
print(anw(5))
print(anw2(3))

