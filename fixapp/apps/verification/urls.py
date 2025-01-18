from django.urls import path
from .views import verify_user_view

urlpatterns = [
    path('verify-user/', verify_user_view, name='verify_user'),
]
