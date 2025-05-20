from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.contrib import admin

USER_OPTIONS = (
    ('user', 'user'),
    ('admin', 'admin'),
    ('super-admin', 'super-admin'),
)

# Create your models here.

class CustomUser(AbstractUser):
    special_user = models.CharField(max_length=20, choices= USER_OPTIONS, default= 'user')
    name = models.CharField(max_length=50, default='Anonymous')
    phone = models.CharField(max_length = 15, default='1234567890')
    email = models.EmailField(max_length=254, unique=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

    date_of_birth = models.DateField(null=True, blank=True)


    # Override groups and user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Provide unique related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Provide unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )


    def __str__(self):
        return f'{self.username} - {self.name} - {self.email}'
    
    # change customer to customers in admin panel
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        unique_together = ('email', 'username')

@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
        "address",
        "profile_picture",
    )

