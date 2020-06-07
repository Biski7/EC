# Create your views here
from django.shortcuts import render
from .models import *

from django.views.generic.base import View


class BaseView(View):
    view = {}

class HomeView(BaseView):
     def get(self,request):
         self.view['items'] = Item.objects.all()
         self.view['sliders'] = Slider.objects.all()
         self.view['category'] = Category.objects.all()
         self.view['subcategory'] = SubCategory.objects.all()
         self.view['ad'] = Ad.objects.all()
         return render(self.request, 'index.html', self.view)



# def aboutview(request):
#     return render(request, 'about.html')
#
# def portfolioview(request):
#     return render(request, 'portfolio.html')
#
# def priceview(request):
#     return render(request, 'price.html')
#
# def servicesview(request):
#     return render(request, 'services.html')
