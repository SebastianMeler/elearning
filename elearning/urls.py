from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from courses.views import CourseListView

urlpatterns = [
    url(r'accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    url(r'^course/', include('courses.urls')),
    url(r'^$', CourseListView.as_view(), name='course_list'),
    url(r'^students/', include('students.urls')),
]
