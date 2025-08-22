
from django.urls import path
#from .views import list_books, LibraryDetailView
from django.urls.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('book_list/', views.list_books, name='book_list'),
    path('library/books/', views.LibraryDetailView.as_view(), name='library_details'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('admin/', views.admin_view, name='admin'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('member/', views.member_view, name='member'),
]