
from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('book_list/', views.list_books, name='book_list'),
    path('library/books/', views.LibraryDetailView.as_view(), name='library_details'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout')
]