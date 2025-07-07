from api.models import Client, Exercise, Trainer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import  viewsets
from api.serializers import ClientSerializer, ExerciseSerializer, TrainingSerializer
# Create your views here.

class ClientViewSet (viewsets.ModelViewSet):
    queryset= Client.objects.all()
    serializer_class=ClientSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['age','sex','weight']

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset= Exercise.objects.all()
    serializer_class=ExerciseSerializer


class TrainerViewSet (viewsets.ModelViewSet):
    queryset= Trainer.objects.all()
    serializer_class=TrainingSerializer
    def perform_create(self, serializer):
        c=Client.objects.get(id=self.request.data.get('c_id'))
        e=Exercise.objects.get(id=self.request.data.get('ex_id'))
        c.exercises.add(e)
        