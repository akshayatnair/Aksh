def student_discount(price):
    x=price-(price*10)/100
    return x
def regular_discount(newprice):
    y=newprice-(newprice*5)/100
    return y
selling_price=int(input("enter the selling price"))
final_price=regular_discount(student_discount(selling_price))
print(final_price)
