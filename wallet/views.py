from django.shortcuts import render
from rest_framework import generics
from .models import DigitalWallet


class WalletAPIView(generics.ListAPIView):
    pass

    
