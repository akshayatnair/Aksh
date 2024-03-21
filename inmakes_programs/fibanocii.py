def fibanocii(x):
   if  x <= 1:
     return x
   else:
       return(fibanocii(x-1)+fibanocii(x-2))
nterms=13
if nterms <= 0:
    print("enter a positive integer")
else:
    print("fibanocii series is:")
    for i in range(nterms):
        print(fibanocii(i))


