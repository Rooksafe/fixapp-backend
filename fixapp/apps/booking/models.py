from django.db import models
from users.models import Client, Professional

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# cambiar nombre de la clase
class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply')
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='apply')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('open', 'Open'),
            ('Close', 'Closed'),
        ],
        default='open')
    
    def __str__(self):
        return f"{self.professional.user.username} - {self.job.title}"