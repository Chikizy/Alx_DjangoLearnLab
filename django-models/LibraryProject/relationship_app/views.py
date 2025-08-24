from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required, user_passes_test

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list' : books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.book_set.all()
        return context 

#class CustomLoginView(LoginView):
#    template_name = 'relationship/login.html'
#    redirect_authenticated_user = True
#    success_url = reverse_lazy('home')

#class CustomLogoutView(LogoutView):
#    template_name = 'relationship_app/logout.html'

# class registerView(CreateView):
#    form_class = UserCreationForm
#    template_name = 'relationship_app/register.html'
#    success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form' : form})

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

#Role protected views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
 
 
 ##############
 #updating views to enforce permissions
 @permisssion_required('relationship_app.can_add_book')
 def add_book(request):
     #logic

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    #logic
    
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    #logic