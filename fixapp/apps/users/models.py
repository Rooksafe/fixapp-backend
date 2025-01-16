from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('professional', 'Professional'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professional_profile')
    bio = models.TextField()
    is_verified = models.BooleanField(default=False)
    verification_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('verified', 'Verified'),
            ('rejected', 'Rejected'),
        ],
        default='pending'
    )
    
# @receiver(post_save, sender=User)
# def create_or_update_professional_profile(sender, instance, created, **kwargs):
#     if instance.role == 'professional':
#         Professional.objects.get_or_create(user=instance)

# Modificadooo!!!
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'professional':
            Professional.objects.get_or_create(user=instance)
        elif instance.role == 'user':
            Client.objects.get_or_create(user=instance)