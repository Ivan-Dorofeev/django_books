from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from books.models import Book

from books.forms import BookForm


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'books_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["town"] = False
        return context

class BookDetaiView(generic.DetailView):
    model = Book
    context_object_name = 'book_detail'
    template_name = 'book_detail.html'


def add_new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                group=form.cleaned_data['group'],
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
            )
            return HttpResponseRedirect(reverse('books'))

    else:
        form = BookForm()
        return render(request, 'book_add.html', {'form': form})


def change_book(request, pk):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.filter(id=pk).update(
                group=form.cleaned_data['group'],
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
            )
            return HttpResponseRedirect(reverse('books'))

    else:
        form = BookForm()
        return render(request, 'book_change.html', {'form': form})
