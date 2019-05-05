from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book

# Create your views here.
def index(request):
    mybooks_list = Book.objects.order_by('title')
    context = {'mybooks_list': mybooks_list}
    return render(request, 'mybooks/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'mybooks/detail.html', {'book': book})