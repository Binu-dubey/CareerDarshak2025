"""
URL configuration for careerDarshak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Assessment import views as assessment_views 
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordResetForm
from django.contrib.auth.views import LogoutView 
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('careerlibrary/', include('careerlibrary.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('fullresult/',views.fullresult,name='fullresult'),
    path('contact/',views.contact,name='contact'),
    path('privacy/',views.privacy,name='privacy'),
    path('condition/',views.condition,name='condition'),

    
    # Authentication URLs
    path('registration/',views.RegistrationView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='website/login.html',authentication_form=LoginForm, next_page='home'), name='login'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='website/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='website/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view (template_name ='website/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view (template_name ='website/password_reset_done.html'),  name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view (template_name ='website/password_reset_confirm.html', form_class=MySetPasswordResetForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view (template_name ='website/password_reset_complete.html'), name='password_reset_complete'),
    path('Assessment/', include('Assessment.urls')),
    

    path('level1/', include('level1.urls')),

    path("__reload__/",include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
