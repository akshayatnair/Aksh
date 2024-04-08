from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Item

# Create your views here.
def home(request):
   obj=Place.objects.all()
   obj1 = Item.objects.all()
   return render(request, "index.html", {'result': obj,'res':obj1})


#def contact(request):

# def about(request):

   #return render(request,"contact.html")
#def detail(request):
  # return render(request,"detail.html")
#def thanks(request):
  # return HttpResponse("Thank you,Please Visit Again")