from django.urls import path
from .views import CategoryListView, ProfessionalListView, JobListView, JobDetailView, ApplicationListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('professionals/', ProfessionalListView.as_view(), name='professional_list'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    # path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
]
