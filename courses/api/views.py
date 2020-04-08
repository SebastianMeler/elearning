from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .permissions import IsEnrolled
from .serializers import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer
from ..models import Subject, Course


class SubjectListView(generics.ListAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

	@action(
		methods=['post'],
		authentication_classes=[BasicAuthentication],
		permission_classes=[IsAuthenticated],
		detail=True
	)
	def enroll(self, request, *args, **kwargs):
		course = self.get_object()
		course.students.add(request.user)
		return Response({'enrolled': True})

	@action(
		detail=True,
		methods=['get'],
		serializer_class=CourseWithContentsSerializer,
		authentication_classes=[BasicAuthentication],
		permission_classes=[IsAuthenticated, IsEnrolled]
	)
	def contents(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
