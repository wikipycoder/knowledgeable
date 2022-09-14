from rest_framework import serializers
from .models import DigitalWallet


class DigitalWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = DigitalWallet
        fields = "__all__"

    

