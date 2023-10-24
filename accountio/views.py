from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accountio.models import User
from accountio.serializers import PublicUserRegistrationSerializer, PrivateUserLoginSerializer

# Create your views here.
class PublicUserRegistration(APIView):
    def post(self, request, formate=None):
        serializer =PublicUserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'status':'Registration succesful'}, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class PrivateUserLogin(APIView):
    def post(self, request, formate =None):
        serializer = PrivateUserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            # checking if the email exist in the database or not.
            email = serializer.data.get('email')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user=None

            if user:
                    return Response({"success": "User Logged in Successfully"}, status= status.HTTP_201_CREATED)
            else:
                return Response({"status": "Email not matched"}, status= status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
