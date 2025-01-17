
from django.urls import path,include
from . import views
app_name = 'careerlibrary'

urlpatterns = [
 
    path('', views.library, name='library'),
    path('<int:career_id>/', views.career_detail, name='career_detail'),
    path('branch<int:branch_id>/', views.branch_detail, name='branch_detail'),
    path('path<int:branch_id>/', views.path, name='pathbook'),
]
