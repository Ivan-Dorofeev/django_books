from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from books import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/detail/<pk>/', views.BookDetaiView.as_view(), name='book_detail'),
    path('books/add/', views.add_new_book, name='book_add'),
    path('books/change/<pk>/', views.change_book, name='book_change'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
