from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, work_email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if work_email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(work_email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, work_email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, work_email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Country(models.Model):
    
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.country
    
class State(models.Model):
    
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.state       

class City(models.Model):

    city = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.city
    

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class Departement(models.Model):
    
    departement = models.CharField(max_length=20)

    def __str__(self):
        return self.departement

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, unique=True, db_index=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    work_email = models.EmailField(max_length=255, unique=True, db_index=True)
    personal_email = models.EmailField(max_length=255, unique=True, db_index=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('work_email'))

    USERNAME_FIELD = 'work_email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.work_email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
class Period(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shift = models.TextField()
    
    # def __str__(self):
    #     return self.created_at
     

class Product(models.Model):
    title = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title
    
    
class Reparation(models.Model):
    issue = models.TextField()
    support_person = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Person {self.support_person} period {self.period} and {self.product}"
    
    