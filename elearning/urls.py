from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
