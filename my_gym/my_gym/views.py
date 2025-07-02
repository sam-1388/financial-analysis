from django.shortcuts import render, redirect
from my_gym.forms import RegisterForm, CompleteForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from my_gym.models import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class home(APIView):
    def get(self,request):
        return Response({'message': 'welcome to our site!!'}, status=status.HTTP_200_OK)
    def post(self,request):
        xusername = request.data.get('xusername')
        password = request.data.get('password')
        return Response({'message': f'Account for {xusername} created successfully!'}, status=201)
      

          
class login(APIView):
    def post(self,request):
          xemail=request.data.get('email')   
          xpassword=request.data.get('password')
          return Response({'message': f'welcome back {xemail} to our site'},status=status.HTTP_200_OK)
   
          
           
class workout(APIView):
    def post(self,request):
        try:
            sets = int(request.data.get('sets', 0))
            reps = int(request.data.get('reps', 0))
            weight = int(request.data.get('weight', 0))

            volume = sets * reps * weight

            if volume == 0:
                message = ""
            elif volume < 1000:
                message = "Keep going! You're building consistency."
            elif volume < 2000:
                message = "Nice work! Your training volume looks solid."
            else:
                message = "Beast mode! Excellent job pushing your limits."

            return Response({'volume': volume, 'message': message}, status=status.HTTP_200_OK)

        except (TypeError, ValueError):
            return Response({'error': 'Invalid input. Please enter valid numbers.'}, status=status.HTTP_400_BAD_REQUEST)
