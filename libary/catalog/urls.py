from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.index, name='index'),
]


urlpatterns += [
    url('books/', views.BookListView.as_view(), name='books'),
]


urlpatterns += [
    url('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]


urlpatterns += [
    url('author/', views.AuthorListView.as_view(), name='author')
]