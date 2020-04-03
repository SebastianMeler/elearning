from django.conf.urls import url
from . import views

app_name = 'students'

urlpatterns = [
	url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
	url(r'^enroll-course/$', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
]
