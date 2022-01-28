from django.urls import path, re_path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='book'),
    path('authors/', views.Author.as_view(), name='authors'),
    # path('book/<int:id>/', views.DetailBook.as_view(), name='book=detail'),
    path('book/<str:pk>/', views.DetailBook.as_view(), name='book-detail'),
    path('authors/<int:id>/', views.detail_authors),
    # path('book/<int:id>/', views.book, name='book-detail'),
]

