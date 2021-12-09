from django.urls import path
from . import  views

urlpatterns = [
    path('cadastro/', views.Produto_Add),
    path('produtos/',views.Produto_View),
    path('update/<int:id>',views.Produto_Update)

]