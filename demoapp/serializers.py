from rest_framework import serializers
from .models import assignments,submission

# Serializer for 'assignments' model
class demoAppSerializer(serializers.ModelSerializer):

	class Meta:
		model = assignments
		fields = ('id','heading')

# Serializer for 'submission' model
class demoAppSubSerializer(serializers.ModelSerializer):

	class Meta:
		model = submission
		fields = ('id','title','description','assignment')