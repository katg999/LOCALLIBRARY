from django.urls import path
from . import views
#from django.views.generic import RedirectView
#from django.views.generic import RedirectView



urlpatterns = [
    path('', views.index, name='index'),
    #path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.book_renew_librarian, name='book-renew-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]

