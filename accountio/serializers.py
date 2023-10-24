from rest_framework import serializers
from accountio.models import User

class PublicUserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields=['email', 'name', 'password', 'confirm_password']

    def validate(self, attr):
        password = attr.get('password')
        password2 = attr.get('confirm_password')
        if password != password2:
            return serializers.ValidationError("password not matched")
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class PrivateUserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ['email','password']