from django.urls import path,include

from . import views

urlpatterns = [
  path('lista/',views.lista,name='lista'),
  path('creat/',views.creat,name='creat'),
  path('adicionar/',views.adicionar,name='adicionar')
]
