from django.shortcuts import render
from .models import Book, Author,BookInstance,Genero
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instancias = BookInstance.objects.all().count()

    num_instancias_available  = BookInstance.objects.filter(status__exact='a').count()

    num_autores = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instancias': num_instancias,
        'um_instancias_available': num_instancias_available,
        'num_authors': num_autores,
    }

    return render(request,'index.html',context=context)