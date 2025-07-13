from django.urls import  path, include
from rest_framework import routers
from .views import ClientViewSet, ExerciseViewSet ,TrainerViewSet
router=routers.DefaultRouter()
router.register(r"clients",ClientViewSet)
router.register(r"exercises",ExerciseViewSet)
router.register(r"training",TrainerViewSet)