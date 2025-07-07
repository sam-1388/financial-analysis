from rest_framework import serializers
from .models import Client,Exercise, Trainer

class ExerciseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name']


class ClientSerializer (serializers.ModelSerializer):
    exercises = ExerciseNameSerializer(many=True, read_only=True) 
    class Meta:
        model=Client
        fields='__all__'
        read_only_fields=['exercises']
        

class ExerciseSerializer (serializers.ModelSerializer):
    class Meta:
        model=Exercise
        fields='__all__'


        
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__' 