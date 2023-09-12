from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserAccounManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

class UserAccount(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tokenValidation = models.CharField(max_length=255, null=True, blank=True)
    first_login = models.BooleanField(default=True)
    recuperationCode = models.CharField(max_length=255, null=True, blank=True)

    objects = UserAccounManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
    
class Error(models.Model):
    error = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, default='Error users')

    def __str__(self):
        return self.name