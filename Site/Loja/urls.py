from django.urls import path
from . import  views

urlpatterns = [
    path('',views.inicio),
    path('cadastro/', views.Produto_Add,name='Produto_Add'),
    path('produto_view/',views.Produto_View, name='Produto_View'),
    path('update/<int:id>',views.Produto_Update)

]