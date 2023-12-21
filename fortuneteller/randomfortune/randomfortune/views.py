from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
  fortune = random.choice(fortuneList)
  context = {"fortune" : fortune }
  return render(request,"randomfortune/fortune.html", context)

fortuneList = ["Your life just got easier","Boom! Position filled - Django - Michael Scott","You will make a good decision today","A X Factor is stepping into your life"]
