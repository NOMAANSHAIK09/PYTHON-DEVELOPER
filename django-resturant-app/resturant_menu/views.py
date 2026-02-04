from django.shortcuts import render
from django.views import generic
from .models import item, MEAL_TYPE


class Menulist(generic.ListView):
   queryset=item.objects.order_by('-date_created')
   template_name="index.html"

   def get_context_data(self,**kwargs):
       context=super().get_context_data(**kwargs)
       context["meals"]=MEAL_TYPE


       return context


class Menuitemdetail(generic.DetailView):

    model=item
    template_name="detail.html"
    pass
    