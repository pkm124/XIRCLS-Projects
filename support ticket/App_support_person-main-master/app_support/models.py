from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, unique=True, db_index=True)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True, db_index=True, null=True)
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    IN_REVIEW = 'In Review'
    DONE = 'Done'
    
   
class Campany(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
       
class Customer(User):
    
    def __str__(self):
        return f"Customer {self.username}"
 
class Subject(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Campany, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Company {self.company}"   

    
class TicketSupport(models.Model):
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    suject = models.ForeignKey(Subject, on_delete=models.CASCADE)