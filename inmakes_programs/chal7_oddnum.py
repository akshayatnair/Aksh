#odd=[]
#for i in range(3,100):
    #if i % 2 != 0:
        #odd.append(i)
#print("all the odd numbers from 3 to 99 \n ",odd)


odd=[ i for i in range(3,100) if i%2!=0]
print("odd numbers between 3 to 100 are \n",odd)