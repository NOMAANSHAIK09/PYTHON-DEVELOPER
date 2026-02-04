from django.urls import path
from . import views
urlpatterns = [
    path('',views.Menulist.as_view(),name='home'),
    path('item/<int:pk>/',views.Menuitemdetail.as_view(),name='menu_item'),
]