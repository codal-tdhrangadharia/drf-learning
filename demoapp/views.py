from rest_framework import viewsets
from .models import assignments, submission
from .serializers import demoAppSerializer, demoAppSubSerializer

# View for 'assignment' model
class assignmentList(viewsets.ModelViewSet):
	queryset = assignments.objects.all()
	serializer_class = demoAppSerializer

# View for 'submission' model
class submissionList(viewsets.ModelViewSet):
	queryset = submission.objects.all()
	serializer_class = demoAppSubSerializer