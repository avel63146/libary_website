from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]


urlpatterns += [
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]


urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='author')
]


