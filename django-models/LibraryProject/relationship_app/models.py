from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = (('can_add_book', 'can add book'),
                       ('can_change_book', 'can change book'),
                       ('can_delete_book', 'can delete book'))
    

    def _str_(name):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def _str_(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_choices = [('Admin', 'Admin'),
                    ('Librarian', 'Librarian'), 
                    ('Member', 'Member'),]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        else:
            instance.userprofile.save()