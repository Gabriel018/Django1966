
from django.shortcuts import render, redirect
from .models import Produto
from .ProdutoForm import Formulario_Produto
# Create your views here.

def Produto_Add(request):

    #Cria um docionario
    dados = {}
     #adiciona os dados ao dicionario
    form  = Formulario_Produto(request.POST or None)
    if form.is_valid():
        form.save()
        redirect('/')
    dados['form']= form

    return render(request,'index.html',dados)

def Produto_View(request):

    produto = Produto.objects.all()

    dado = {
         'produtos':produto
    }
    return render(request, 'index.html',dado)


def Produto_Update(request,id):

    produto = Produto.objects.get(id=id)
    form = Formulario_Produto(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'index.html', {'form': form, 'produto': produto})