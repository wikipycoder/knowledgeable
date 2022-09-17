from rest_framework.serializers import ModelSerializer
from .models import User
from wallet.models import DigitalWallet

class RegisterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    
    def create(self, validated_data):
        
        password = validated_data.get("password")
        wallet = DigitalWallet.objects.create()
        validated_data["wallet"] = wallet
        user = User(**validated_data)
        if password:
            user.set_password(password)
            user.save()
            return user


        return None


class UpdateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]
        extra_kwargs = {

            "first_name": {"required": False},
            "last_name": {"required": False},
            "email": {"required": False},
            "username": {"required": False},
            "password": {"required": False}
        }

    def update(self, instance, validated_data):
        print("do you get hit")
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        password = validated_data.get("password")
        if password:
            instance.set_password(password)
        

        instance.save()
        return instance


class UserDataSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username"]