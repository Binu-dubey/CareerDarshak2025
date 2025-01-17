from django.urls import path
from . import views
from .views import UserProfileView 




urlpatterns = [
    # path('registration/', views.StudentRegistrationView.as_view(), name='customerregistration'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='userprofile'),
    path('assessment/', views.assessment, name='assessment'),
    path('psychometric/', views.psychometric_test, name='psychometric_test'),
    path('aptitude/', views.aptitude_test, name='aptitude_test'),
    path('reasoning/', views.reasoning_test, name='reasoning_test'),
    path('complete/', views.assessment_complete, name='assessment_complete'),
    
]
