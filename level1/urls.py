from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.level1_intro, name='level1_intro'),
    path('level1/', views.level1_view, name='level1'),
    path('submit/', views.submit_level1, name='submit_level1'),
    path('personality_assessment_result/', views.personality_assessment_result, name='personality_assessment_result'),

    path('level1_result/', views.level1_result, name='level1_result'),

]
